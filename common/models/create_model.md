flask-sqlacodegen "mysql://root:@127.0.0.1/food_db" --tables member --outfile "common/models/member/Member.py" --flask

flask-sqlacodegen "mysql://root:@127.0.0.1/food_db" --tables oauth_member_bind --outfile "common/models/member/OauthMemberBind.py" --flask