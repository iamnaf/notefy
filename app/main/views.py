from datetime import datetime
from flask import (render_template, 
                    session, flash, 
                    redirect, 
                    url_for,
                    jsonify)
from . import main
from .forms import CommentForm, NoteForm
from .. import db
from ..models import Note

@main.route('/', methods=['GET', 'POST'])
def index():
    notes = Note.query.order_by(Note.pub_date.desc()).all()
    # return render_template('index.html', current_time=datetime.utcnow(), notes=notes)
    note_list = []
    note_dict = {}
    for note in notes:
        note_dict['author']=note.author
        note_dict['title']=note.title
        note_dict['body']=note.body
        note_dict['pub_date']=note.pub_date
        note_list.append(note_dict)
    return jsonify(note_list)

# @main.route('/note_view/<id>', methods=['get', 'post'])
# def note_view(id):
#     comment = CommentForm()
#     post = Note.query.filter_by(id=id).first()
    # return render_template('note_view.html', post=post)
    

@main.route("/create", methods=['GET', 'POST'])
def create_note():
    note = NoteForm()
    if note.validate_on_submit():
        # title = Note(title=note.title.data)
        # author = Note(author=note.author.data)
        # body = Note(body=note.body.data)
        # pub_date = Note(pub_date=datetime.utcnow())
        note_post = Note(title=note.title.data, 
                         body=note.body.data,
                         author=note.author.data,
                         pub_date=datetime.utcnow())
        # db.session.add(title)
        # db.session.add(author)
        # db.session.add(body)
        # db.session.add(pub_date)
        db.session.add(note_post)
        db.session.commit()
        flash("New Note Submitted.")
        return redirect(url_for('main.index'))
    # return render_template('create_note.html', note=note)
    return jsonify(title=note.title.data, 
                    body=note.body.data, 
                    author=note.author.data,
                    pub_date=datetime.utcnow())