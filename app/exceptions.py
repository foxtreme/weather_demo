class DecodingError(ValueError):

    def __init__(self, description):
        self._description = "The response text could not be decoded. description: {description}".format(
            description=description
        )

    @property
    def description(self):
        return self._description
