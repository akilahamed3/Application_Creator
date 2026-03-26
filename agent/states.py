from pydantic import BaseModel, Field

class File(BaseModel):
    path: str = Field(description ="The path of the file to be created or modified")
    purpose: str =Field(description ="The purpose of the file e.g. 'main application logic', 'data processing module' etc")

class Plan(BaseModel):
    name: str = Field(description="The name of app to be built")
    description: str = Field(description = "A one line description of the app to be built e.g. 'A web application for managing person'")
    techstack: str = Field(description = "the tech stack to be used for the app e.g. 'python', 'javascript', 'react' etc")
    features: list[str] = Field(description = "A list of features the app should have e.g. 'user authentication', 'data visualization', 'logs' etc")
    files: list[File] = Field(description = "A list of files to be created, each with a 'path' and 'purpose'")