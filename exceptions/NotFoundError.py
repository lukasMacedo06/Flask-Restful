from .BaseError import BaseError

class NotFoundError(BaseError):

	def __init__(self, message='Not Found'):
		BaseError.__init__(self)
		self.status = 404
		self.message = message