from flask import Flask

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
	SITE_NAME = "DataFam",
	SITE_DESCRIPTION = "A forum free from Java nonsense.",
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db' #relative pass to physical db location (this has 4 /)
)
