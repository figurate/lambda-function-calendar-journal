from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.integration import SNS
from diagrams.aws.network import APIGateway

with Diagram("Calendar Journal", show=False, direction="TB"):

    journal = Lambda("calendar journal")
    topic = SNS("calendar topic")

    APIGateway("journal api") >> journal >> DynamodbTable("journal entries") >> journal
    journal >> topic
