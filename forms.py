from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField,HiddenField,IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Logar')

class RegisterUserForm(FlaskForm):
    username = StringField('Usuário',validators=[DataRequired()])
    first_name = StringField('Primeiro Nome',validators=[DataRequired()])
    last_name = StringField('Último Nome',validators=[DataRequired()])
    address = StringField('Endereço',validators=[DataRequired()])
    city = StringField('Cidade',validators=[DataRequired()])
    country = StringField('País',validators=[DataRequired()])
    post_code = StringField('Código Postal',validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Registar')

class VagasForm(FlaskForm):
    titulo_vaga = StringField('Titulo Vaga',validators=[DataRequired()])
    categoria_vaga = StringField('Categoria Vaga',validators=[DataRequired()])
    area_candidatura  = StringField('Area Candidatura',validators=[DataRequired()])
    descricao_vaga = StringField('Descrição Vaga',validators=[DataRequired()])
    tipo_vaga = StringField('Tipo Vaga',validators=[DataRequired()])
    requisitos_vaga = StringField('Requisitos Vaga',validators=[DataRequired()])
    perfil_candidato = StringField('Perfil Candidato',validators=[DataRequired()])
    habilitacoes = StringField('Habilitações',validators=[DataRequired()])
    provincia_vaga = StringField('Província Vaga',validators=[DataRequired()])
    nivel_ingles_vaga = StringField('Nivel Ingles Vaga',validators=[DataRequired()])
    habilidades_exigida = StringField('Habilidades Exigida',validators=[DataRequired()])
    experiencia_profissional = StringField('Experiencia Profissional',validators=[DataRequired()])
    anos_exp_exigida = StringField('Anos Exp. Exigida',validators=[DataRequired()])
    data_inicio_vaga = StringField('Data Início',validators=[DataRequired()])
    data_termino_vaga = StringField('Data Término',validators=[DataRequired()])
    submit = SubmitField('Registar')


