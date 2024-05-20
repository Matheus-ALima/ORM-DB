from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])

#usuario = Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha="1234567")
#print("Novo usuario:", usuario.id, usuario.nome, usuario.email)

#usuario = Usuario.create(nome="Guilherme", email="guilherme@teste.com", senha="1234567")
#usuario = Usuario.create(nome="Joao", email="joao@teste.com", senha="1234567")
#usuario = Usuario.create(nome="Maria", email="maria@teste.com", senha="1234567")

#lista_usuarios = Usuario.select()
#print("Listando Usuarios: ")

#for u in lista_usuarios:
#    print("-", u.id, u.nome, u.email)

#usuario1 = Usuario.get(Usuario.id == 1)
#print("usuario pelo id", usuario1.id, usuario1.nome)

#joao = Usuario.get(Usuario.email == "joao@teste.com")
#print("Usuario: ", joao.id, joao.nome, joao.email)

#maria = Usuario.get( Usuario.email == "maria@teste.com")
#maria.nome = "Maria Python"
#maria.save()

#print("Alterao com sucesso: ", maria.id, maria.nome, maria.email)

#print("Tentando criar um usuario com email duplicado")

#try:
#    usuaraio_duplicado = Usuario.create(nome = "Duplicado", email = "teste@teste.com", senha ="123456")
#except:
#    print("Email já exitente, tente novamente")

#usuario_deletado.delete_instance()
#usuario_deletado = Usuario.get(Usuario.email == "teste@teste.com")
#
#try:
    #Usuario.get( Usuario.email == "teste@teste.com")
#except:
    #print("Usuario deletado")

#maria = Usuario.get( Usuario.email == "maria@teste.com")

#anuncio = Anuncio.create(
#    usuario = maria,
#    titulo = "Video de banco de dados",
#    descricao = "O projeto seria criar um video sobrte canco de dados e ORM com python",
#    valor = 500.0
#)

#print("Novo anuncio: ", anuncio.id, anuncio.titulo)

#Anuncio.create(usuario = maria,titulo = "Anuncio 1",descricao = "Deixa o like",valor = 1000.0)
#Anuncio.create(usuario = maria,titulo = "Anuncio 2",descricao = "Faça um comentario",valor = 5000.0)
#Anuncio.create(usuario = maria,titulo = "Anuncio 3",descricao = "Se inscreva",valor = 1500.0)

#print("anuncios da maria:")
#
# anuncios_maria = Anuncio.select().join(Usuario).where(Usuario.email == "maria@teste.com")
#
# for a in anuncios_maria:
#
#     print("-", a.id, a.titulo, a.valor)

Anuncio.delete().execute()
print("Quantidade de anuncios: ", Anuncio.select().count())