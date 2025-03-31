import zipfile
import wget



# download dos arquivos
wget.download("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", "anexo1.pdf"),
wget.download("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf", "anexo2.pdf")


# nome do zip

zipfilename = "compactados.zip"

# zipa os arquivos

with zipfile.ZipFile(zipfilename, 'w') as zipf:
    zipf.write("anexo1.pdf") 
    zipf.write("anexo2.pdf") 
