

from django.urls import path
from techapp.views import pick_and_speech,index,speed_typing,photography,ppt,madad,quiz,video,stressinterview,treasurehunt,model,code

urlpatterns = [
   path("pick_and_speech/",pick_and_speech,name="pick_and_speech"),
   path("speed_typing/",speed_typing,name="speed_typing"),
   path("photography/",photography,name="photography"),
   path("ppt/",ppt,name="ppt"),
   path("madad/",madad,name="madad"),
   path("quiz/",quiz,name="quiz"),
   path("video/",video,name="video"),
   path("stressinterview/",stressinterview,name="stressinterview"),
   path("treasurehunt/",treasurehunt,name="treasurehunt"),
   path("model/",model,name="model"),
   path("code/",code,name="code"),
   path("",index,name="index"),
]
