from app import create_app

if __name__=="__main__":
    # app from appfactory
    create_app().run(host="0.0.0.0", port=6000, debug=True)