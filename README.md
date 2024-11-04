# Frontend
- vue-vite template:
`yarn create vite my-vue-app --template vue-ts`
- pinia
- tailwind

- To run dev:
    - run `cd frontend`
    - run `yarn install`
    - run `yarn dev`

    - make sure there is an `.env.local` file that has variables `VITE_API_URL` and `VITE_FUNCTION_HOST_KEY` (the latter can be empty)

# Backend
- Flask
- Azure Functions

Flask with Azure Functions:
https://learn.microsoft.com/en-us/samples/azure-samples/flask-app-on-azure-functions/azure-functions-python-create-flask-app/

- To run backend
    - make sure to have azure build tools installed
    - run `cd backend`
    - run `pip install -r requirements.txt`
    - run `func start`

# Deployment
- Github Actions workflows
- Azure Functions for backend and Azure Static Web Apps for frontend
