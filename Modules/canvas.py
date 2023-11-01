import tkinter as tk


def create_app():
    app = tk.Tk()
    app.geometry("800x600+400+150")
    app.title("Shop")
    app.configure(bg='grey')
    return app


root = create_app()
