from flask import render_template, session, request, redirect, uel_for

from shop import app, db

@app.route('/')
def home():
    return "Home page of shop"