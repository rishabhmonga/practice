def modelNames(callog):
    delimitedCal = callog.split('Name=')
    print(delimitedCal)
    for model in delimitedCal:
        print(model.split('&')[0])


if __name__ == '__main__':
    score_input = "msg=Name=ARSVarsInteg&status=0**Name=uELV&status=0&model_score1=634.0&model_score2=3.5033154416019396**Name=ATOM15MODEL&status=0&model_score1=0.0014400381522583965**Name=UELV15V1&status=0&model_score1=624.0&model_score2=0.052361915351162545**Name=MM15MODEL&status=0&model_score1=-999.0&model_score3=-999.0&model_score2=0**Name=UBSM15&status=0&model_score1=0.002270108139751269**Name=CAM15V1_DCC&status=0&model_score1=8.298028025766457E-4**Name=CAM15V1_INELIGIBLE&status=0&model_score1=0.020670740688925552**Name=COLLUSION15&status=0&model_score1=0.005472862343359545**Name=ARM14DUMMYUNMODEL&status=0&model_score1=600.2825147128751&model_score2=4.267478086121891**Name=ARM14DUMMYNNMODEL&status=0&model_score1=0.3820475475251808**Name=ARM14DUMMYMODEL&status=0&model_score1=600.2825147128751&model_score3=606.0&model_score2=636&model_score4=0.3820475475251808**Name=BSM15MODEL&status=0&model_score1=0.374608251158529**Name=ARM14UNMODEL&status=0&model_score1=600.2825147128751&model_score2=4.267478086121891**Name=ARM14NNMODEL&status=0&model_score1=0.5934044552911797**Name=ARM14MODEL&status=0&model_score1=600.2825147128751&model_score3=639.0&model_score2=683&model_score4=0.5934044552911797**Name=CAM15V2_BASE&status=0&model_score1=9.314290031024921E-4**Name=CAM15V2_CB&status=0&model_score1=8.230178003823469E-5**Name=CAM15V2_LR&status=0&model_score1=438.0**Name=CAM15V2_EMS&status=0&model_score1=431.0**Name=ARM15TP_LR&status=0&model_score1=657.0**Name=ARM15TP_NN&status=0&model_score1=0.342825719836622**Name=ARM15TP_FU&status=0&model_score1=541**Name=MM16_EBAY&status=0&model_score1=0.12654166307069897&model_score2=0.0**Name=MM16&status=0&model_score1=0.0016104334147522094&model_score2=-999.0**Name=ATOM16&status=0&model_score1=0.0**Name=CAM16_GBT_V1&status=0&model_score1=7.431703818229905**Name=CLV16_STV&status=0&model_score1=0.016473629274693**Name=CLV16_TPV&status=0&model_score1=278.0**Name=MM16_EBAY_V2_EMS&status=0&model_score1=0.00810736015772728**Name=ATOM16V2_SEG2_CT&status=0&model_score1=0.0**Name=ATOM16V2_SEG2_RT&status=0&model_score1=0.0**Name=ATOM16V2_SEG2&status=0&model_score1=0.0**Name=CFASBRE16&status=0&model_score1=408.0**Name=UBSM16&status=0&model_score1=0.0037229576230459467**Name=BSM16&status=0&model_score1=0.046971561093601566**Name=ARM16TP_BASE&status=0&model_score1=27.0**Name=ARM16TP_ADV&status=0&model_score1=70.0**Name=ARM16TP_EMS&status=0&model_score1=48.5**Name=ATOM_SEG3_S1&status=0&model_score1=1.0**Name=ATOM_SEG3_S2&status=0&model_score1=0.016473629274693**Name=ATOM_SEG3_S3&status=0&model_score1=0.016473629274693**Name=CAM16_GBT_V2&status=0&model_score1=11.085069119913086**Name=CV_1ST_SEND_POS&status=0&model_score1=0.30252191069405554**Name=CV_1ST_SEND_NEG&status=0&model_score1=1.3883889906389884**Name=CV_1ST_SEND_BINARY&status=0&model_score1=909.5065675816733**Name=CLV17_1ST_SEND&status=0&model_score1=0.8680727965495175**Name=ARM17_NCG&status=0&model_score1=94.91468740645506**Name=ARM17_CG&status=0&model_score1=4.831199043431255**Name=ARM17&status=0&model_score1=518.7235046060905**Name=MM17&status=0&model_score1=0.019382569402041534&model_score2=-999.0**Name=SAM17&status=0&model_score1=0.016473629274693&model_score2=-999.0**Name=RUCS_POC_MODEL&status=0&model_score1=81.0**Name=CAM17_GBT_V1&status=0&model_score1=17.25687307736798**Name=CAM17_V2_SHIFU_GBT_1&status=0&model_score1=540.1803268034631**Name=CAM17_V2_SHIFU_GBT_2&status=0&model_score1=492.63331327140287**Name=CAM17_V2_SHIFU_GBT_3&status=0&model_score1=542.3256853409201**Name=CAM17_V2_NN_1&status=0&model_score1=4.792420243637195**Name=CAM17_V2_NN_2&status=0&model_score1=0.471116648221374**Name=CAM17_V2_NN_3&status=0&model_score1=11.915460388664433**Name=CAM17_V2_NN_4&status=0&model_score1=21.0**Name=CAM17_V2_H2O_GBT_1&status=0&model_score1=10.858252106531355**Name=CAM17_V2_H2O_GBT_2&status=0&model_score1=16.207754503070916**Name=CAM17_V2_EMS&status=0&model_score1=359.0**Name=ATOM17V1_SEG2_CT&status=0&model_score1=3.0**Name=ATOM17V1_SEG2_RT&status=0&model_score1=2.0**Name=ATOM17V1_SEG2&status=0&model_score1="
    modelNames(score_input)