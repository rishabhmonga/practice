import csv
from collections import Counter


def varCount(sample, vars):
    var_count = Counter()

    with open(sample) as f_sample:
        sampleReader = csv.reader(f_sample)
        for row in sampleReader:
            if len(row[0].split('.')) > 1:
                var = row[0].split('.')[1]
                var_count[var] += 1

    with open(vars) as f_vars:
        sampleReader = csv.reader(f_vars)
        for row in sampleReader:
            var_count[row[0]] += 1

    return var_count


if __name__ == '__main__':
    # with open('/Users/rismonga/Documents/var2.csv', 'rb') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=',')
    # for row in spamreader:
    #     print
    #     ', '.join(row)

    var1 = '/Users/rismonga/Documents/var1.csv'

    var2 = '/Users/rismonga/Documents/var2.csv'

    var3 = '/Users/rismonga/Documents/var3.csv'

    orig = '/Users/rismonga/Documents/ZootVariables.csv'

    verify_count = Counter()

    var_count = varCount(var1, orig)

    # print(var_count.items())

    for i in var_count.items():
        if i[1] > 1:
            # print(i[0])
            verify_count[i[0]] += 1

    # print()
    # print('#'*20)
    # print()
    # for i in var_count.items():
    #     if i[1] == 1:
    #         print(i[0])
    #

    var_count = varCount(var2, orig)

    for i in var_count.items():
        if i[1] > 1:
            # print(i[0])
            verify_count[i[0]] += 1

    var_count = varCount(var3, orig)

    for i in var_count.items():
        if i[1] > 1:
            # print(i[0])
            verify_count[i[0]] += 1
        elif i[1] <= 1:
            print(i[0])

    # final
    # for i in verify_count.items():
    #     if i[1] > 0:
    #         print(i[0])


"""
Variables being used

ratio_sum_ss_AchAll_dly_3m_lx
dsc_achRetS_NSF_lx
sum_ss_All_dly_sc_sd_All
ratio_sum_ss_All_3m12m
u_ppdaysonfile
s_cc_pct_credit
ratio_sum_ss_Mobile_dly_12m
CREDIT_CARD_cnt
dsc_neg_bal
topamt_ind_amt
S_CC_D_SINCE_LATEST_1ST_CHG
sum_ss_All_dly_12mth
sum_ss_AchAll_dly_3mth
num_ss_All_dly_sc_achret
num_ach_chg_12m
num_rstr_12m
s_cc_pct_credit_lx
ratio_r_sum_ss_Ach_3m12m_lx
TOTAL_SENT_CNT
s_cc_pct_failed_auth_lx
s_cc_d_since_oldest
sum_ss_CC_dly_sc_sd_CC
"""

"""
variables not being used

cc6_aa_code1
CC_TYPE_WORST_NEW
longest_bank_days_confirmed
ratio_n_days_in_negpos_bal_3m
cc6_segment_id
num_rs_All_dly_3mth
sum_withdraw_dly_3mth
avg_daily_bal_12m_lx
num_ss_All_dly_12mth_lx
longest_bank_days
num_sd_CC_dly_1mth
num_days_in_pos_bal_12m
num_addCC_All_1mth
num_rvr_12mth
num_addACH_All_12mth
avg_daily_bal_3m
cc6_score
MOA_V_MOALife
TOTAL_SENT_TPV
num_days_in_neg_bal_12m
sum_withdraw_dly_12m
cc6_segment_name
max_ss_All_mth_12m
num_clr_3mth
dsc_sr
ratio_num_srSsAll_1m
cc6_sr_prob
cc6_policy_segment
longest_cc_days_created
STD_TXNS
sum_ss_All_dly_12mth_lx
num_days_in_pos_bal_12m_lx
expectedTagName
model_status_CFAN
CFAN_model_score_1
CFAN_model_segment
CITRUSUK_model_score_1
CITRUSUK_model_segment_2
model_status_CFAS
CFASDA_model_score
CFASDA_model_segment
model_status_PLUTO
OnboardingSegment
cc_type_worst
RANK_HIGHLEVEL
STATUS_HIGHLEVEL
SELLER_INFO_ATTR_FINAL
std_txns
OnboardingType
CreditPrimaryActorType
FlowSource
CreditAuthenticationType
"""