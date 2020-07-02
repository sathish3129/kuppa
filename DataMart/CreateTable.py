"""
CREATE TABLE tutorials_tbl(
   -> tutorial_id INT NOT NULL AUTO_INCREMENT,
   -> tutorial_title VARCHAR(100) NOT NULL,
   -> tutorial_author VARCHAR(40) NOT NULL,
   -> submission_date DATE,
   -> PRIMARY KEY ( tutorial_id )
   -> );

"""


class CreateTable:
    """This is a docstring. I have created a new class"""

    def __init__(self, header=None):
        self.pk = None
        self.header = header

    def primary_key(self, field_name=None):
        if self.header is not None and field_name is not None:
            self.pk = field_name

