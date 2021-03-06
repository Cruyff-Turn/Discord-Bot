import discord
import re

class ReactionNotifier:
    _RL_PATTERN = r"\:rl\:"
    RL_TEAM_SIZE = 3

    def get_unique_users(self, post_user, user_list):
        users = []
        for user in user_list:
            users.append(user)

        if post_user not in users:
            users.append(post_user)

        return users

    def is_rl_gathered(self, reaction, users):
        unique_users = self.get_unique_users(reaction.message.author, users)

        if unique_users and len(unique_users) >= self.RL_TEAM_SIZE * 2:
            return self._create_gathered_message(reaction, unique_users)
        else:
            return None

    def is_rl_reaction(self, reaction):
        return re.search(self._RL_PATTERN, str(reaction.emoji))

    def _create_gathered_message(self, reaction, user_names):
        mes = '\n'.join([user.mention for user in user_names])
        return str(self.RL_TEAM_SIZE * 2) + "人集まりました" + str(reaction.emoji) + "\n" + mes + "\n"
