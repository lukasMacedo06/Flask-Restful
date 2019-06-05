class BaseError(Exception):

	def __init__(self, status=400, message=''):
		Exception.__init__(self)
		self.status = status
		self.message = message

	def to_dict(self):
		return {
			'error': {
				'status_code': self.status,
				'message': self.message
			}
		}
