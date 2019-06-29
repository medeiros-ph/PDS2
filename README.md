# Projeto de Processamento de Sinais 2

Discente: Raphael Medeiros :: 1421824GELT;
Docente: Aline Gesualdi;
CEFET/RJ - Celso Suckow da Fonseca :: UNED Maracanã
Apoio: Laboratório de Processamento de Sinais e Instrumentação (LAPSI)
Rio de Janeiro, Junho de 2019.

# Introdução: 

Este projeto tem por objetivo desenvolver de forma prática os conhecimentos adquiridos com a disciplina de PDS2.
Utilizaremos uma placa embarcada e uma câmera para aquisição das imagens em tempo real e processamento. Tendo como objetivo identificar as características de um determinado objeto, mostrar na tela alguns parâmetros e uma quadrado no meio da tela para busca do objeto (dizer se o mesmo se encontra ou não).


# Instalações:

Download Virtual Box - https://www.virtualbox.org/wiki/Downloads

Download the Virtual Machine OVA file: https://drive.google.com/file/d/1_5gZ2-GQCrg9RuRMMeHIkg3cN2E_nK_Y/view

Instruções para instalar o OpenCV no Raspberry Pi no arquivo "packages".

pip install numpy
pip install matplotlib
pip install opencv-contrib-python
pip install dlib


# Metodologia:

Software:

Why OpenCV in Python?

* Python is one of the easiest languages for beginners;
* It is extremely powerful for Data Science and Machine Learning;
* Is stores images in numpy arrays which allows us to do some very powerful operations quite easily.

Python versão 2.7: Anaconda Package is preferred but not required.
OpenCV versão 2.14.3

Hardware:

* NVIDIA Jetson TK1;
* Câmera Logitech c930 - HD1080p;

# Futuro do projeto:

Seguir e/ou buscar o alvo (Tracking) com uso servo motores (pantilt) como suporte para a câmera.

# Referências: 
Material de PDS 2:
https://app.schoology.com/course/1978377466/materials

Curso da Udemy de PDI com Raspberry Pi:
https://www.udemy.com/image-processing-on-raspberry-pi/

Curso da Udemy de CV com OpenCV com Python:
https://www.udemy.com/master-computer-vision-with-opencv-in-python/

