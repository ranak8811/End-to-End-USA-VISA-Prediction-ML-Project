from us_visa.pipline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()



# ---------------------------------------------------------------------


# from us_visa.logger import logging

# logging.info("Logging has started")


# ---------------------------------------------------------------------


# from us_visa.exception import USvisaException
# from us_visa.logger import logging
# import sys

# try:
#     r = 10 / 0
#     print(r)

# except Exception as e:
#     raise USvisaException(e, sys)

# ---------------------------------------------------------------------

# import os
# from dotenv import load_dotenv

# load_dotenv()

# mongodb_url = os.getenv("MONGODB_URL")
# print(mongodb_url)


