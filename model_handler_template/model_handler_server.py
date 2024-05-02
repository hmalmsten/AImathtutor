import grpc.aio as grpc
from concurrent import futures
import asyncio
import random

# import the generated classes :
import model_handler_pb2
import model_handler_pb2_grpc

port = 8061

class ModelHandler(model_handler_pb2_grpc.ModelHandlerServicer):
  def __init__(self):
    # self.model_list = [
    #   {
    #       'needs_text': True,
    #       'needs_image': False,
    #       'can_text': True,
    #       'can_image': False,
    #       'modelID': 'model_1'
    #   },
    #   {
    #       'needs_text': False,
    #       'needs_image': True,
    #       'can_text': False,
    #       'can_image': True,
    #       'modelID': 'model_2'
    #   },
    #   {
    #       'needs_text': True,
    #       'needs_image': True,
    #       'can_text': True,
    #       'can_image': True,
    #       'modelID': 'model_3'
    #   }
    # ]
    self.model_list = []

  def startTask(self, request, context):
    suitable_models_list = []

    #Scan in the model list for the suitable model
    for model in self.model_list:
      if (request.needs_text and request.needs_image):
        if (model["can_text"] and model["can_image"]):
          suitable_models_list.append(model)
      elif (request.needs_text):
        if (model["can_text"] and not model["needs_image"]):
          suitable_models_list.append(model)
      elif (request.needs_image):
        if (model["can_image"] and not model["needs_text"]):
          suitable_models_list.append(model)

    #choose a random model if there are multiple that sastisfy the requirements
    chosen_model = random.choice(suitable_models_list)
    print(chosen_model)

    #assign the modelID to the session
    request.session["modelID"] = chosen_model["modelID"]
    
    return model_handler_pb2.Empty()

  def finishTask(self, request, context):
    taskMetrics = request
    metrics = model_handler_pb2.metricsJson()
    return model_handler_pb2.metricsJson()
  
  def sendToModel(self, request, context):
    taskRequest = request
    return
  
  def returnToTask(self, request, context):
    modelAnwer = request
    return
  
  def registerModel(self, request, context):
    #add the models to the model list on startup
    self.model_list.append(request)
    return model_handler_pb2.Empty();

async def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  model_handler_pb2_grpc.add_ModelHandlerServicer_to_server(ModelHandler(), server)
  print("Starting the model handler server. Listening on port : " + str(port))
  server.add_insecure_port("0.0.0.0:{}".format(port))
  await server.start()
  await server.wait_for_termination()

asyncio.run(serve())
