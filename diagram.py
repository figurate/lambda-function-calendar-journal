from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.network import APIGateway

with Diagram("Calendar Journal", show=False, direction="TB"):

    APIGateway("journal api") >> Lambda("calendar journal") >> DynamodbTable("journal entries")
