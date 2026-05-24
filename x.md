🏢 EmployerProfile

user (OneToOne) — владелец компании / работодатель  
company_name — название компании  
description — описание компании  
logo — логотип компании  
website — сайт компании  
location — местоположение компании  
created_at — дата создания профиля компании
👤 User

username — логин пользователя  
email — почта пользователя  
password — пароль  
role — роль пользователя (seeker/employer)  
image — аватар пользователя  
phone — номер телефона  
date_joined — дата регистрации
👨‍💻 SeekerProfile

user (OneToOne) — владелец профиля  
bio — информация о пользователе  
skills — навыки пользователя  
resume — PDF резюме  
experience — опыт работы  
education — образование  
birth_date — дата рождения  
location — город проживания
💼 Job

company (ForeignKey) — компания которая создала вакансию  
title — название вакансии  
description — полное описание вакансии  
salary — зарплата  
location — место работы  
job_type — тип работы (full time / part time / remote)  
experience_required — требуемый опыт  
category (ForeignKey) — категория вакансии  
created_at — дата публикации  
deadline — срок окончания вакансии  
is_active — активна ли вакансия
📂 Category

name — название категории  
icon — иконка категории  
description — описание категории
📩 Application

job (ForeignKey) — вакансия  
user (ForeignKey) — кто откликнулся  
message — сообщение работодателю  
resume — резюме при отклике  
status — статус заявки (pending/accepted/rejected)  
created_at — дата отклика
⭐ FavoriteJob

user (ForeignKey) — пользователь  
job (ForeignKey) — избранная вакансия  
created_at — дата добавления в избранное