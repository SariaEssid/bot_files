*********************************************************************************************************
text.split("concernant")[0].strip()

*********************************************************************************************************
{BOT_MESSAGES.get('error_model_connexion')}

*********************************************************************************************************
detail_level, last_intent = get_detaillevel_lastintent(action_label, tracker)

*********************************************************************************************************
last_last_user_question, last_answer = None, None

☠


*********************************************************************************************************
maintained_intent = intent
            ***

            if intent and intent == ActiveIntents.NLU_FALLBACK.value:
                PDF_PATH = get_file_path(last_intent, INTENT_MAP_PG_INFO, settings.PATH_HIERARCY_ALL)
                maintained_intent = last_intent
                log_info_text("🔁 🔁 🔁 🔁 🔁  CATCHA-2.2 : ", str(last_intent))

            log_info_text(action_label, f"🔁 🔁 🔁 🔁 🔁  CATCHA - maintained_intent : {maintained_intent}")
			
*********************************************************************************************************			
action_label, start_time, question, last_second_question, payload_tech_error, user_id, session_id, confidence, intent = load_util_values(tracker, ActionsLabel.PY_RESPOND_FROM_PDF_FOR_ADVICES.value)			


*********************************************************************************************************
log_info_text("SPECIALITIES DIRECT : ", json.dumps(pos_spec_by_sessions, indent=2, ensure_ascii=False))


log_info_text(action_label, f"🔁 🔁 🔁 🔁 🔁  CATCHA-1 {str(last_intent)}")
log_info_text(action_label, f"🔁 🔁 🔁 🔁 🔁  CATCHA-2 - maintained_intent : {maintained_intent}")
log_info_text(action_label, f"🔁 🔁 🔁 🔁 🔁  CATCHA-3 {last_sscomp_value}")



DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
FILE_PATH = settings.BASE_KNOWLEDGE_TEXT # Read the file once at startup
with open(FILE_PATH, "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f.readlines() if line.strip()]