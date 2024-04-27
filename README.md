# Django Text_to_Image
This Django application generates images using the Stabilit AI Text-to-image generation API. This project uses Celery for parallel processing to manage asynchronous calls to the API.
## Installation
1. Clone the repository:

    git clone https://github.com/your_username/chaotix-ai.git

2. Install dependencies:

    pip install -r requirements.txt

3. Set up your environment variables:
    
      Go to settings.py and set STABILITY_API_KEY variable
   #### STABILITY_API_KEY: Your Stabilit AI API key


# Running the Application
1. Start the Celery worker:
   
     celery -A chaotix worker --loglevel=info
   
2. Start the Django development server:

    python manage.py runserver

3. Access the application at http://localhost:8000.

4. Use the application to trigger the generation of images using the provided text prompts.


# Testing the Application

1. Open Postman and create a new request.
   
2. Set the request type to POST and enter the API endpoint for image generation:

``` http://localhost:8000/api/generate_image/ ```

3. Add the following JSON payload to the request body to specify the text prompts and image size:

```
{
    "text_prompts": [
        "A red flying dog",
        "A husky ninja",
        "A footballer kid",
        "A wizard on Mars",
        "Baby Dragon"
    ],
    "image_size": "1024x1024"
}
```

4. Click on the "Send" button to submit the request.
   
5. Check the response to ensure that the image generation request is successful. The response should contain a message indicating that the request is submitted along with the request ID.
   
![Screenshot 2024-04-28 002847](https://github.com/adnansaifi123/chaotix_text_to_image/assets/67619920/4d3aab89-fb16-49d8-8f63-bacaec51e2ab)

# GET Request (Retrieve Generated Images)

1. Create a new request in Postman.

2. Set the request type to GET and enter the API endpoint to retrieve the generated images:
```http://localhost:8000/api/generate_image/```

3. Click on the "Send" button to submit the request.

4. Check the response to ensure that the images are retrieved successfully. The response contains image data, created_at, text_promt.

   ![Screenshot 2024-04-28 002941](https://github.com/adnansaifi123/chaotix_text_to_image/assets/67619920/489c6d6c-0557-4a47-a866-942d593bb0c2)

# Using Web API
1. Use HTTP client or browser to send a POST request to the API endpoint:
```http://localhost:8000/api/generate_image/```

2. Submit the request and check the response for the status and any relevant information returned by the API.
   ![Screenshot_28-4-2024_02724_127 0 0 1](https://github.com/adnansaifi123/chaotix_text_to_image/assets/67619920/9e42d235-2252-4bdd-ba15-8ea3cab6c74d)
