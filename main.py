from website import create_app


app = create_app()
if __name__ == '__main__': #ensure that server only runs when main.py is directly running
    app.run(debug=True) #start up web server, debug=true to ensure auto update (dev purpose only)