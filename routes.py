from cmath import e
from queue import Empty
from site import venv
from flask import Blueprint, render_template, session, redirect, flash, url_for,request
from front_env.api.candidate_client import CandidateClient
from front_env.api.vagas_client import VagasClient
from front_env.api.curriculum_client import CurriculumClient
from front_env.api.user_client import UserClient
from flask_login import current_user
from front_env.machine.df_vagas import *
from front_env.machine import *
from front_env.machine.columns import *
from front_env.machine.constantes import *
from front_env.machine.algoritmo_machine_learning import ReturnCandidatesIds
from front_env.machine.utils_cand import *
import forms
import os

blueprint = Blueprint('frontend',__name__,url_prefix='/api/frontend')



ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','.docx'}

UPLOAD_FOLDER = "./static/uploads/"

@blueprint.route('/login', methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    api_key = UserClient.login(form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']
                return redirect(url_for('frontend.profile'))
            else:
                flash('Cannot Login')
        else:
            flash('Cannot Login')
    return render_template('login_form.html',form=form)

#logging out
@blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('frontend.login'))

#registering a user
@blueprint.route('/register_user', methods=['POST','GET'])
def register_user():
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()

        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
    
    form=forms.RegisterUserForm(request.form)
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                username = form.username.data
                if UserClient.user_exists(username):
                    flash("Please try another user name")
                    return render_template('register_user.html', form=form)
                else:
                    user = UserClient.create_user(form)
                    if user:
                        return redirect(url_for('frontend.login'))
            else:
                flash("Errors")
        except e:
            print(e)
    return render_template('register_user.html',form=form,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])


@blueprint.route('/profile', methods=['GET','POST'])
def profile():
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}

    if not current_user.is_authenticated:
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()

        except:
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}

    username= session['user']['username']
    first_name= session['user']['first_name']
    last_name= session['user']['last_name']
    address= session['user']['address']
    city= session['user']['city']
    country= session['user']['country']
    post_code = session['user']['post_code']
    return render_template('profile.html',username=username, first_name=first_name, last_name=last_name,address=address,city=city,country=country,post_code=post_code, count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums)



#getting all vagas
@blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = {}
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        users = UserClient.get_users()
        try:
            users = UserClient.get_users()
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            users = {'result':[]}
            return render_template('list_users.html',users=users,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])
    return render_template('list_users.html',users=users,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])

@blueprint.route('/users', methods=['GET'])
def list_users():
    return render_template('view_user.html')


#getting an vaga id
@blueprint.route('/users/view/<id_user>', methods=['GET','PUT'])
def get_id_user(id_user):
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}

    user = UserClient.get_user_id(id_user)
    if user:
        user = UserClient.get_user_id(id_user)
    else:
        user = {'result':[]}
    return render_template("view_user.html", user=user, candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])



#updating candidato
@blueprint.route('/users/update/<id_user>', methods=['GET','POST','PUT'])
def update_user(id_user):
    form = None
    id_user = request.form['id_user']
    if request.method == "POST":
        try:
            form = {'username': request.form['username'],
                    'first_name': request.form['first_name'],
                    'last_name':request.form['last_name'],
                    'address': request.form['address'],
                    'city': request.form['city'],
                    'country': request.form['country'],
                    'post_code': request.form['post_code'],
                    'password': request.form['password']
            }
            update_user = UserClient.update_user(form,id_user)
            if update_user:
                redirect('api/frontend/users')
        except e:
            print(e)
    else:
        print("Envie os dados apartir do formulário!")
    return redirect('/api/frontend/users')


#getting an vaga id
@blueprint.route('/users/view_delete/<id_user>', methods=['GET'])
def user_id_delete(id_user):
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}

    user = UserClient.get_user_id(id_user)
    if user:
        user = UserClient.get_user_id(id_user)
    else:
        user = {'result':[]}
    return render_template("view_delete_user.html", user=user, candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])

#deleting an user id
@blueprint.route('/users/delete/<id_user>', methods=['GET','POST','DELETE'])
def delete_id_user(id_user):
    if request.method == 'POST':
        try:
            id_user = request.form['id_user']
            id_user = UserClient.delete_user_id(id_user)
            if id_user:
                redirect('api/frontend/users')
            else:
                print("Usuário não existe!")
        except e:
            print(e)
    return redirect('/api/frontend/users')


#getting all candidates
@blueprint.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_candidates()
        try:
            candidates = CandidateClient.get_candidates()
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
            return render_template('list_candidates.html',candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])
    return render_template('list_candidates.html',candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])


##################################################################C
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#registering candidates
@blueprint.route('/register_candidate', methods=['POST','GET'])
def register_candidate():
    if request.method == 'POST':
        form = {
            'nome_completo':request.form["nome_completo"],
            'data_nascimento':request.form["data_nascimento"],
            'natural_de':request.form["natural_de"],
            'genero':request.form["genero"],
            'n_bilhete':request.form["n_bilhete"],
            'provincia_residencia':request.form["provincia_residencia"],
            'telemovel_principal':request.form["telemovel_principal"],
            'email':request.form["email"],
            'habilitacoes_academica':request.form["habilitacoes_academica"],
            'instituicao':request.form["instituicao"],
            'curso':request.form["curso"],
            'ano_conclusao':request.form["ano_conclusao"],
            'media_final':request.form["media_final"],
            'area_candidatura':request.form["area_candidatura"],
            'ano_experiencia_area':request.form["ano_experiencia_area"],
            'disponibilidade':request.form["disponibilidade"],
            'nivel_ingles':request.form["nivel_ingles"]
        }

        if form is not Empty():
            try:
                curriculum = request.files["curriculum"]
                filename = curriculum.filename
                curriculum.save(os.path.join(UPLOAD_FOLDER, curriculum.filename))
                cv = curriculum.filename
                form["curriculum"] = cv

                candidate = CandidateClient.create_candidate(form)
                if candidate:
                    #pegamos o id do candidato cadastrado
                    id_candidato = candidate["result"]["id_candidato"]
                    #pegamos o caminho do curriculum
                    cv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), UPLOAD_FOLDER , curriculum.filename)
                    #aqui estamos a pegar os dados dos candidatos
                    curriculum = extract_text_from_pdf(cv_path)
                    #aqui vamos extrair as habilidades dos candidatos
                    habilidades = extract_skills(curriculum)
                    #extraindo a descrição da vaga
                    vaga_pontuacao = extract_vagas_pontuacao(curriculum)

                    #salavando os dados do curriculum
                    form_aux = {"id_candidato": id_candidato, "curriculum":filename, "habilidades":habilidades, "vaga_pontuacao":vaga_pontuacao}
                    curriculum = CurriculumClient.create_curriculum(form_aux)
                    if curriculum:
                        flash("Curriculum criado com sucesso!")
                    flash("Candidato Criado com Sucesso.")
                    return redirect(url_for('frontend.register_candidate'))
            except e:
                print(e)
        else:
                flash("Erro ao tentar criar um novo candidato")
    return render_template('register_candidate.html')

#updating candidato
@blueprint.route('/candidates/update/<id_candidato>', methods=['GET','POST','PUT'])
def update_candidate(id_candidato):
    form = None
    id_candidato = request.form['id_candidato']
    if request.method == "POST":
        try:
            form = {'nome_completo': request.form['nome_completo'],
                    'genero': request.form['genero'],
                    'instituicao':request.form['instituicao'],
                    'curso': request.form['curso'],
                    'nivel_ingles': request.form['nivel_ingles'],
                    'provincia_residencia': request.form['provincia_residencia']
            }
            update_candidato = CandidateClient.update_candidate(form,id_candidato)
            if update_candidato:
                redirect('api/frontend/candidates')
        except e:
            print(e)
    else:
        print("Envie os dados apartir do formulário!")
    return redirect('/api/frontend/candidates')


#getting an vaga id
@blueprint.route('/candidates/view/<id_candidate>', methods=['GET','PUT'])
def get_id_candidate(id_candidate):
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}

    candidate = CandidateClient.get_cand_id(id_candidate)
    if candidate:
        candidate = CandidateClient.get_cand_id(id_candidate)
    else:
        candidate = {'result':[]}
    return render_template("view_candidate.html", candidate=candidate, candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])


#getting an vaga id
@blueprint.route('/candidates/view_delete/<id_candidate>', methods=['GET'])
def cand_id_delete(id_candidate):
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}

    candidate = CandidateClient.get_cand_id(id_candidate)
    if candidate:
        candidate = CandidateClient.get_cand_id(id_candidate)
    else:
        candidate = {'result':[]}
    return render_template("view_delete.html", candidate=candidate, candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])

#deleting an candidate id
@blueprint.route('/candidates/delete/<id_candidato>', methods=['GET','POST','DELETE'])
def delete_id_candidate(id_candidato):
    if request.method == 'POST':
        try:
            id_candidato = request.form['id_candidato']
            candidate = CandidateClient.delete_cand_id(id_candidato)
            if candidate:
                redirect('api/frontend/candidates')
            else:
                print("Candidato não existe!")
        except e:
            print(e)
    return redirect('/api/frontend/candidates')

############################################# VAGAS #######################################################
    
#registering vaga
@blueprint.route('/register_vaga', methods=['POST','GET'])
def register_vaga():
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
        
        form=forms.VagasForm(request.form)
        if request.method == 'POST':
            if form.validate_on_submit():
                vaga = VagasClient.create_vagas(form)
                if vaga:
                    flash("Vaga Criada com Sucesso.")
                    return redirect(url_for('frontend.register_vaga'))
            else:
                flash("Erro ao tentar criar uma nova vaga")
    return render_template('register_vagas.html', form=form,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])

#updating vagas
@blueprint.route('/vagas/update_vaga/<id_vaga>', methods=['GET','POST','PUT'])
def update_vaga(id_vaga):
    form = None
    if request.method == "POST": 
        try:
            id_vaga= request.form['id_vaga']
            form = {'titulo_Vaga':request.form["titulo_Vaga"],
                        'categoria_vaga':request.form["categoria_vaga"],
                        'tipo_vaga':request.form["tipo_vaga"],
                        'descricao_vaga':request.form["descricao_vaga"],
                        'requisitos_vaga':request.form["requisitos_vaga"],
                        'anos_exp_exigida':request.form["anos_exp_exigida"],
                        'experiencia_profissional':request.form["experiencia_profissional"],
                        'area_candidatura':request.form["area_candidatura"],
                        'perfil_candidato':request.form["perfil_candidato"],
                        'habilitacoes':request.form["habilitacoes"],
                        'provincia_vaga':request.form["provincia_vaga"],
                        'nivel_ingles_vaga':request.form["nivel_ingles_vaga"],
                        'habilidades_exigida':request.form["habilidades_exigida"],
                        'data_inicio_vaga':request.form["data_inicio_vaga"],
                        'data_termino_vaga':request.form["data_termino_vaga"]}
            update_vaga = VagasClient.update_vagas(form,id_vaga)
            if update_vaga:
                redirect('api/frontend/vagas')
        except e:
            print(e)
    return redirect('/api/frontend/vagas')

#getting all vagas
@blueprint.route('/vagas', methods=['GET'])
def get_all_vagas():
    vagas = {}
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
        
    if not current_user.is_authenticated:
        vagas = VagasClient.get_vagas()
        try:
            vagas = VagasClient.get_vagas()
        except:
            vagas = {'result':[]}
            return render_template('list_Vagas.html',vagas=vagas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])
    return render_template('list_vagas.html',vagas=vagas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums,username=session['user']['username'])

#getting an vaga id
@blueprint.route('/vagas/view/<id_vaga>', methods=['GET'])
def get_id_vaga(id_vaga):
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    vagas = VagasClient.get_vaga_id(id_vaga)
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            vagas = VagasClient.get_vaga_id(id_vaga)
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
        return render_template('view_vaga.html',vagas=vagas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])
    return render_template('view_vaga.html',vagas=vagas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums= count_curriculums,username=session['user']['username'])


#getting an vaga id
@blueprint.route('/vagas/view_delete/<id_vaga>', methods=['GET','PUT'])
def delete_get_vaga(id_vaga):
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    vagas = VagasClient.get_vaga_id(id_vaga)
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
            vagas = VagasClient.get_vaga_id(id_vaga)
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
        return render_template('view_vaga_delete.html',vagas=vagas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])
    return render_template('view_vaga_delete.html',vagas=vagas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums,username=session['user']['username'])

#deleting an vaga id
@blueprint.route('/vagas/delete/<id_vaga>', methods=['GET','POST','DELETE'])
def delete_id_vaga(id_vaga):
    if request.method == 'POST':
        id_vaga = request.form['id_vaga']
        vaga = VagasClient.delete_vaga_id(id_vaga)
        if vaga:
            redirect('api/frontend/vagas')
        else:
            print("Candidato não existe!")
    return redirect('/api/frontend/vagas')

########################################################################MACHINE LEARNING##########################################################################
#função de classificação
def ListaClassificacao(lista_provincias,lista_ano_experiencias,lista_habilitacoes,lista_disponibilidades,lista_nivel_ingles):
    #variaveis
    valor_porcentagem1 =  0
    valor_porcentagem2 = 0
    contador = 0
    #lista de classificações
    classificacao_provincias,classificacao_habilitacoes,classificacao_ano_experiencias,classificacao_disponibilidade,classificacao_nivel_ingels =([] for i in range(5))
    #aumentando a porcentagem em função da província
    for pv in lista_provincias:
        if pv in PROVINCIA:
            valor_porcentagem1 = contador + 1
            classificacao_provincias.append(valor_porcentagem1)
        else:
            valor_porcentagem2 = contador + 0
            classificacao_provincias.append(valor_porcentagem2)
    #definindo o valor de percentagem do ano de experiência
    for ano in lista_ano_experiencias:
        if ano in ANO_EXPERIENCIA:
            valor_porcentagem1 = contador + 1
            classificacao_ano_experiencias.append(valor_porcentagem1)
        else:
            valor_porcentagem2 =  contador + 0
            classificacao_ano_experiencias.append(valor_porcentagem2)
    #aumentando a porcentagem em função das habilitações 
    for hb in lista_habilitacoes:
        if hb in HABILITACOES:
            valor_porcentagem1 = contador + 1
            classificacao_habilitacoes.append(valor_porcentagem1)
        else:
            valor_porcentagem2 = contador + 0
            classificacao_habilitacoes.append(valor_porcentagem2)
    #aumentando a porcentagem em função da disponibilidade
    for dp in lista_disponibilidades:
        if dp in TIPO_VAGA:
            valor_porcentagem1 = contador + 1
            classificacao_disponibilidade.append(valor_porcentagem1)
        else:
            valor_porcentagem2 = contador + 0
            classificacao_disponibilidade.append(valor_porcentagem2)
    #aumentando a porcentagem em função da lingua
    for lg in lista_nivel_ingles:
        if lg in NIVEL_INGLES:
            valor_porcentagem1 = contador + 1
            classificacao_nivel_ingels.append(valor_porcentagem1)
        else:
            valor_porcentagem2 = contador + 0
            classificacao_nivel_ingels.append(valor_porcentagem2)

    #soma das listas de classificação
    lista_class1 = [x + y for x, y in zip(classificacao_provincias, classificacao_ano_experiencias)]

    lista_class2 = [x + y for x, y in zip(lista_class1, classificacao_habilitacoes)]
   
    lista_class3 = [x + y for x, y in zip(lista_class2, classificacao_disponibilidade)]

    lista_class4 = [x + y for x, y in zip(lista_class3, classificacao_nivel_ingels)]
    return lista_class4

#função para retornar o estado de classificação
def EstadoClassificacao(lista_porcentagem):
    #definimos a lista de classificação
    lista_classificacao = []
    for lp in lista_porcentagem:
        if lp < 5:
            classificacao1 ="Desclassificado"
            lista_classificacao.append(classificacao1)
        elif lp < 10 :
            classificacao2 ="Moderado"
            lista_classificacao.append(classificacao2)
        elif lp == 10:
            classificacao3 ="Classificado"
            lista_classificacao.append(classificacao3)
        else:
            classificacao4 = "Classificado"
            lista_classificacao.append(classificacao4)
    return lista_classificacao


  
#count how much candidate is there
@blueprint.route('/candidato_classificacao', methods=['GET','POST'])
def candidato_classificacao():
    dataset = {}
    lista_nomes = []
    lista_provincias_2 = []
    lista_habilitacoes_2 = []
    lista_curso = []
    lista_mnivelingles = []


    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}

    #pegando as colunas
    if request.method == "GET":
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
        #vai pegar o id dos candidatos
        get_id = None
        #declaração das listas
        lista_provincias,lista_habilitacoes,lista_ano_experiencias,lista_curriculums=([] for i in range(4))
        lista_disponibilidades,lista_nivel_ingles,list_habilidades,list_vaga_pontuacao,estado_classificacao=([] for i in range(5))

        #pegando as colunas para o algoritmo
        columns = request.args.getlist('coluna')

        #lista com o id dos candidatos
        id_candidato = ['id_candidato']
        #lista_valores
        lista_valores = id_candidato + columns

        ids = ReturnCandidatesIds(lista_valores)
        
        #pondo os dados na base de dados e pondo nas listas  
        for id_cand in ids:
            curriculum_id = CurriculumClient.get_curr_id(id_cand)
            if id_cand:
                get_id = CandidateClient.get_cand_id(id_cand)
                if get_id["result"]:
                    lista_habilitacoes.append(get_id["result"]["habilitacoes_academica"])
                    lista_provincias.append(get_id["result"]["provincia_residencia"])
                    lista_disponibilidades.append(get_id["result"]["disponibilidade"])
                    lista_ano_experiencias.append(get_id["result"]["ano_experiencia_area"])
                    lista_nivel_ingles.append(get_id["result"]["nivel_ingles"])

                    lista_nomes.append(get_id["result"]["nome_completo"])
                    lista_provincias_2.append(get_id["result"]["provincia_residencia"])
                    lista_habilitacoes_2.append(get_id["result"]["habilitacoes_academica"])
                    lista_curso.append(get_id["result"]["curso"])
                    lista_mnivelingles.append(get_id["result"]["nivel_ingles"])

                for hab in curriculum_id["result"]:
                    for hb in curriculum_id["result"]["id_candidato"]:
                        list_habilidades.append(curriculum_id["result"]["habilidades"])
                        list_vaga_pontuacao.append(curriculum_id["result"]["vaga_pontuacao"])
                        lista_curriculums.append(curriculum_id["result"]["curriculum"])

        #chamamos a função de classificacao
        pontuacao = ListaClassificacao(lista_provincias,lista_ano_experiencias,lista_habilitacoes,lista_disponibilidades,lista_nivel_ingles)
        #doing the total classification  
        total_pontuacao = [x + y for x, y in zip(pontuacao,list_vaga_pontuacao)]
        #lista estado de classificacao
        estado_classificacao = EstadoClassificacao(total_pontuacao) 
        dados_candidato = zip(total_pontuacao,estado_classificacao,list_habilidades,lista_nomes,lista_provincias_2,lista_habilitacoes_2,lista_curso,lista_mnivelingles,lista_curriculums)  
    return render_template("candidato_classificacao.html", dados_candidato = dados_candidato,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas, count_curriculums=count_curriculums)

#Configurar colunas
@blueprint.route('/configurar_colunas', methods=['GET'])
def configurar_colunas():
    candidates = {}
    count_candidates = {}
    count_vagas = {}
    count_users = {}
    count_curriculums = {}
    if not current_user.is_authenticated:
        candidates = CandidateClient.get_10_candidates()
        count_candidates = CandidateClient.count_candidates()
        count_vagas = VagasClient.count_vagas()
        count_users = UserClient.count_users()
        count_curriculums = CurriculumClient.count_curriculums()
        try:
            candidates = CandidateClient.get_10_candidates()
            count_candidates = CandidateClient.count_candidates()
            count_vagas = VagasClient.count_vagas()
            count_users = UserClient.count_users()
            count_curriculums = CurriculumClient.count_curriculums()
        except:
            candidates = {'result':[]}
            count_candidates == {'result':[]}
            count_vagas == {'result':[]}
            count_users == {'result':[]}
            count_curriculums == {'result':[]}
        
        colunas = {}
        if not current_user.is_authenticated:
            colunas = ConfigurationColumns()
            try:
                colunas = ConfigurationColumns()
            except:
                colunas = {'result':[]}
            render_template('configurar_algoritmo.html', colunas=colunas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums)
    return render_template('configurar_algoritmo.html', colunas=colunas,candidates=candidates,count_candidates=count_candidates,count_users=count_users,count_vagas=count_vagas,count_curriculums=count_curriculums)

@blueprint.route('/display/<filename>')
def display_file(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


@blueprint.route('/search/<nome_completo>/', methods=['GET','POST'])
def search(nome_completo):
    candidate = CandidateClient.get_cand_nome(nome_completo)
    return render_template('search.html',candidate=candidate)


@blueprint.route('/relatorio_estatistico', methods=['GET','POST'])
def relatorio_estatistico():
    return render_template('relatorio_estatistico.html')