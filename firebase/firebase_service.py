from firebase_admin import messaging

class FirebaseService:
  def send_to_token(self, data, token):
    message = messaging.Notification(title="Chrysus Payment", body=data['message'])
    message = messaging.Message(data=data, token=token, notification=message)
    response = messaging.send(message)
    return response