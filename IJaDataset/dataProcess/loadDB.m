conn = database('bcb','sa','');
conn.Message
selectquery = 'SELECT NAME,STARTLINE,ENDLINE,ID FROM FUNCTIONS WHERE ENDLINE-STARTLINE>20 and ENDLINE-STARTLINE<30 and ID>=000000 and ID<32000000';
data = select(conn,selectquery);
% 12 23