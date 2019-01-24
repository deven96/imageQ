"""@desc 
        Predictors definition -> URL and Upload

     @author 
         Domnan Diretnan
         Artificial Intelligence Enthusiast & Software Engineer.
         Email: diretnandomnan@gmail.com
         Github: https://github.com/deven96
         GitLab: https://gitlab.com/Deven96

     @project
         @create date 2018-12-28 02:03:47
         @modify date 2018-12-28 02:03:47

    @license
        MIT License
        Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """


import urllib3
from ImageQ.processor.base import BasePredictor, RequestHandler

class URLPredictor(BasePredictor):
    """This is a URL class predictor for the ResNet model 

    :param prediction_api: url of the prediction api to send requests to
    :type prediction_api: str
    :param image_url: url to the image to be predicted
    :type image_url: str

    Example:
        >>> predictor = URLPredictor(prediction_api="https://imageqapi.appspot.com/predict", image_url="https://example_image.com/image-jpg")
        >>> predictor.predict()
    """
    def __init__(self, prediction_api, image_url):
        """Constructor method
        """
        self.prediction_api = prediction_api
        self.image_url = image_url
        self.request_handler = RequestHandler(self.image_url, "current")

    @property
    def image_path(self):
        """Image path from url downloaded by urllib3
        
        :returns: path of the image
        :rtype: str
        """
        self.request_handler.save()
        return self.request_handler.image_location


class UploadPredictor(BasePredictor):
    """This is an Upload class predictor for the ResNet model 

    :param image_location: url to the image to be predicted
    :type image_location: str
    """
    pass

