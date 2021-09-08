import pandas as pd
import numpy as np

# exp&ing terminal window to display the df
desired_width = 320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns', 15)

# Cross-referencing champions
chunked_df = pd.read_csv(r'C:\Users\SystemAdmin\PycharmProjects\HelloWorld\statsgg\aggregated_br_data.csv', chunksize=10)

SC = pd.read_csv(r'C:\Users\SystemAdmin\PycharmProjects\HelloWorld\statsgg\Synergies&Counters.csv')

for df in chunked_df:
    first_champ = df.iloc[0]

    if first_champ['win']:  # team1 first player wins
        # **INCREMENTING SYNERGY & SYNTOTAL BY 1**
        for champ in range(0, 5): # ally team
            player = df.iloc[champ]['championName']
            for ally in range(champ):
                allied_champ = df.iloc[ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy + 1, curr_counter, curr_syntotal + 1, curr_ctotal]
            for x_ally in range(champ + 1, 5):
                allied_champ = df.iloc[x_ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy + 1, curr_counter, curr_syntotal + 1, curr_ctotal]
        # ** INCREMENTING COUNTER & COUNTERTOTAL BY 1 **
            for enemy_champ in range(5, 10):  # team 2
                enemy_player = df.iloc[enemy_champ]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter Total']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)] = [1, player, enemy_player, curr_synergy, curr_counter + 1, curr_syntotal, curr_ctotal + 1]
        # ** ENEMY TEAM INCREMENTING DOWN **
        for champ in range(5, 10): # enemy team
            player = df.iloc[champ]['championName']
            for ally in range(5, champ):
                allied_champ = df.iloc[ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy - 1, curr_counter, curr_syntotal + 1, curr_ctotal]
            for x_ally in range(champ + 1, 10):
                allied_champ = df.iloc[x_ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy - 1, curr_counter, curr_syntotal + 1, curr_ctotal]
        # ** INCREMENTING COUNTER & COUNTERTOTAL BY -1 **
            for enemy_champ in range(0, 5): # team 1
                enemy_player = df.iloc[enemy_champ]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter Total']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)] = [1, player, enemy_player, curr_synergy, curr_counter - 1, curr_syntotal, curr_ctotal + 1]

    else:  # team1 loses
        for champ in range(0, 5):  # team 1
            player = df.iloc[champ]['championName']
            # **INCREMENT TEAM SYNERGY BY -1**
            for ally in range(champ):
                allied_champ = df.iloc[ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy - 1, curr_counter, curr_syntotal + 1, curr_ctotal]
            for x_ally in range(champ + 1, 5):
                allied_champ = df.iloc[x_ally]['championName']
                print(SC.loc[(SC['Champion'] == player)])
                print(SC.loc[(SC['Other Champions'] == allied_champ)])
                curr_synergy = SC.loc[(SC['Champion'] == player) & ((SC['Other Champions'] == allied_champ))]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy - 1, curr_counter, curr_syntotal + 1, curr_ctotal]
        # ** INCREMENTING COUNTER & COUNTERTOTAL BY -1 **
            for enemy_champ in range(5, 10):  # team 2
                enemy_player = df.iloc[enemy_champ]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter Total']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)] = [1, player, enemy_player, curr_synergy, curr_counter - 1, curr_syntotal, curr_ctotal + 1]
        # ** ENEMY TEAM INCREMENTING UP **
        for champ in range(5, 10): # enemy team
            player = df.iloc[champ]['championName']
            for ally in range(5, champ):
                allied_champ = df.iloc[ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy + 1, curr_counter, curr_syntotal + 1, curr_ctotal]
            for x_ally in range(champ + 1, 10):
                allied_champ = df.iloc[x_ally]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter Total']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)]['Counter']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == allied_champ)] = [1, player, allied_champ, curr_synergy + 1, curr_counter, curr_syntotal + 1, curr_ctotal]
        # ** INCREMENTING COUNTER & COUNTERTOTAL BY 1 **
            for enemy_champ in range(0, 5): # team 1
                enemy_player = df.iloc[enemy_champ]['championName']
                curr_synergy = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy']
                curr_counter = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter']
                curr_syntotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Synergy Total']
                curr_ctotal = SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)]['Counter Total']
                SC.loc[(SC['Champion'] == player) & (SC['Other Champions'] == enemy_player)] = [1, player, enemy_player, curr_synergy, curr_counter + 1, curr_syntotal, curr_ctotal + 1]

SC.to_csv('S&C.csv')

