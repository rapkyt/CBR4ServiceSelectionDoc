# Outline Tesis Cristian
# A unified model for assessing and selecting heterogeneous services using Case-based reasoning
# Un modelo unificado para evaluar y seleccionar de servicios heterogéneos utilizando Razonamiento basado en casos (CBR)

## Cap1: Intro


### 1.1 Motivación
### 1.2 Organización de la tesis

## Cap2: Background

### 2.1 Intro: outline del capitulo (de que se va a hablar)

### 2.2 Metamodelo (tesis lucas)

### 2.3 CBR for service selection (Paper Clei Alan)

### 2.4 Open Challenges

#### Metamodelo no soportado (sólo wsdl)
#### Aceptar servicios heterogeneos (microservicios // REST)
#### Definir e implementar el proceso apropiadamente
(e.g., usar una base mongo en vez de en memoria; refactorings necesarios?)


## Cap3: Proposal
### Intro (outline del cap)

### 3.1  Mostrar el proceso nuevo (figura draw.io)
#### Explicar cada uno de los pasos a alto nivel
(luego se explicará en detalle en sub-sub-sectio(tn o paragraphs c/u de los pasos)

###  3.2 Explicar el refactoring llevado a cabo respecto de la implementación existente
###  3.3 Explicar el parser de openAPI a metamodelo

### 3.4 Otros aportes

## Cap4: Validación Experimental

### Intro: Explicar a grandes rasgos que exp se van a hacer y qué se va a medir (aprendizaje, precision, over/underfitting?)

### 4.1 "Material" experimental

#### Dataset wsdl
#### Dataset OpenApi
#### De los dos anteriores, se genera el dataset de prueba
#### Base de datos de queries
#### KB a popular

### 4.2 "Proceso" experimental 1

#### Elegir un dataset de muestra inicial para popular la base
#### Calcular precision sin aprendizaje
#### Mutar el dataset inicial y cablear el resultado al servicio relevante
#### Aprender y volver a correr para comparar vs. antes de aprender

### 4.3 "Proceso" experimental 2

#### Experimento con el modelo full (a definir)
#### Cuales son las queries? Deberian ser mutadas automaticamente
#### Cual es el dataset de prueba?

### 4.4 Discussion y "threats to validity" (limitaciones)

## Cap5: Conclusión y trabajos futuros.
