# TpDocker
Tp Docker, cours Intégration Continue

Exercice : Manipulation de base des conteneurs
<br/>
<img width="326" height="138" alt="image" src="https://github.com/user-attachments/assets/f2b00b36-90d2-4d3f-b3c4-57fd24ef0298" />
<br/>
<img width="418" height="117" alt="image" src="https://github.com/user-attachments/assets/0a8801b9-a9e0-4610-a52e-88ad16ce91ef" />
<br/>
<br/>

 Exercice : Création d'un serveur web avec Docker
<br/>
<img width="370" height="134" alt="image" src="https://github.com/user-attachments/assets/72a47987-6e23-4358-bb72-c564713852e1" />
<br/>
<img width="278" height="35" alt="image" src="https://github.com/user-attachments/assets/7ad02c11-32d9-47c1-9090-6a7624ef9fb3" />
<br/>
<img width="688" height="245" alt="image" src="https://github.com/user-attachments/assets/6a916dbc-c514-442c-8224-a187a58552fd" />
<br/>
<br/>

Exercice 5 : Déploiement d'une application Python Flask 
<br/>
<img width="274" height="122" alt="image" src="https://github.com/user-attachments/assets/2a62963b-e969-4d97-86f4-ac77ec0da10a" />
<br/>
ici, on met les ports dans cet ordre pour le run --> port localhost : port python
<br/>
<img width="509" height="260" alt="image" src="https://github.com/user-attachments/assets/9453a609-dfbc-49fb-b684-d655251f1d9b" />
<br/>
cela donne la page web en local suivante :
<br/>
<img width="719" height="87" alt="image" src="https://github.com/user-attachments/assets/f68799ae-4431-4643-ae25-a4510549c4ab" />
<br/>
sans oublier de stopper le conteneur et de le supprimer quand on en a plus besoin
<br/>
<img width="320" height="64" alt="image" src="https://github.com/user-attachments/assets/cb07f2f3-b96c-4e58-bd88-6bc59be91cb2" />
<br/>
<br/>

Exercice 6 : Utilisation de docker compose
<br/>
<img width="434" height="287" alt="image" src="https://github.com/user-attachments/assets/d505160d-a464-4b83-90af-4218c3c21b59" />
<br/>
<img width="651" height="112" alt="image" src="https://github.com/user-attachments/assets/803df45b-ab39-43b3-b60b-155f39712f54" />
<br/>
<br/>

TP OPTIMISATION DOCKER
<br/>
<br/>
on télécharge le dossier zip et on se place dans le bon dossier :
<br/>
<img width="495" height="182" alt="image" src="https://github.com/user-attachments/assets/ba94d54b-d631-4555-aa17-7f0b4660c0d1" />
<br/>
`PS C:\Users\Lucynda\Downloads\tpdockeroptimisation\tpdockeroptimisation> ls     
Répertoire : C:\Users\Lucynda\Downloads\tpdockeroptimisation\tpdockeroptimisation


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        17/09/2025     15:20                node_modules
-a----        17/09/2025     15:19            332 dockerfile
-a----        17/09/2025     15:19          45265 package-lock.json
-a----        17/09/2025     15:19            302 package.json
-a----        17/09/2025     16:03            775 server.js


PS C:\Users\Lucynda\Downloads\tpdockeroptimisation\tpdockeroptimisation> docker build -t opti1 .
[+] Building 5.5s (13/13) FINISHED                                                      docker:desktop-linux
 => [internal] load build definition from dockerfile                                                    0.0s
 => => transferring dockerfile: 371B                                                                    0.0s 
 => [internal] load metadata for docker.io/library/node:latest                                          2.1s 
 => [auth] library/node:pull token for registry-1.docker.io                                             0.0s
 => [internal] load .dockerignore                                                                       0.1s
 => => transferring context: 2B                                                                         0.0s 
 => [1/7] FROM docker.io/library/node:latest@sha256:82a1d74c5988b72e839ac01c5bf0f7879a8ffd14ae40d70080  0.0s 
 => => resolve docker.io/library/node:latest@sha256:82a1d74c5988b72e839ac01c5bf0f7879a8ffd14ae40d70080  0.0s 
 => [internal] load build context                                                                       0.3s 
 => => transferring context: 87.73kB                                                                    0.2s
 => CACHED [2/7] WORKDIR /app                                                                           0.0s 
 => => exporting manifest list sha256:6bdc3d0c0a49ed20e2e1198ddaef307a45a2a32aabcf4eaeffafde8e9b90b442  0.0s 
 => => naming to docker.io/library/opti1:latest                                                         0.0s 
 => => unpacking to docker.io/library/opti1:latest                                                      2.5s `


TOTAL TEMPS : 5.2s 
TAILLE DE L'IMAGE : 1.73GB













