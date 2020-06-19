from chalice import Chalice
import boto3

app = Chalice(app_name='first-app')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/test-ddb')
def test_ddb():
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.get_item(TableName='basicSongsTable', Key={'artist': {'S':'ed sheeran'}, 'song':{'S': 'perfect'}})
    return(response['Item'])
    #table = resource.Table('metadatatable')
    ##result=table.scan()
    #return result


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
