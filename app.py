import streamlit as st
import pandas as pd
import random
import os

# ==========================================
# 0. 数据初始化 (自动生成 ivd_data.csv)
# ==========================================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(CURRENT_DIR, 'ivd_data.csv')

def create_initial_csv():
    """
    如果 CSV 不存在，则创建一个包含 7 大模块核心词汇的初始文件。
    """
    if not os.path.exists(CSV_FILE_PATH):
        # 定义 7 大模块的数据 (IVD 行业专用)
        data = [
            # --- 1. 法规与注册 (RA) ---
            {"module": "1. 法规与注册 (RA)", "term": "Intended Use", "cn": "预期用途", "context": "注册申报核心", "sentence": "The intended use must be clearly defined in the IFU and technical documentation.", "sentence_cn": "预期用途必须在说明书和技术文档中明确定义。"},
            {"module": "1. 法规与注册 (RA)", "term": "Contraindication", "cn": "禁忌症", "context": "安全/风险", "sentence": "Patients with known allergies to the components are listed under contraindications.", "sentence_cn": "对成分已知过敏的患者被列入禁忌症项下。"},
            {"module": "1. 法规与注册 (RA)", "term": "Registrant", "cn": "注册人", "context": "法律主体", "sentence": "The registrant shall submit the annual self-inspection report to the NMPA.", "sentence_cn": "注册人应当向国家药监局提交年度自查报告。"},
            {"module": "1. 法规与注册 (RA)", "term": "Technical Documentation", "cn": "技术文档", "context": "CE/MDR申报", "sentence": "The technical documentation provides evidence of conformity with the general safety and performance requirements.", "sentence_cn": "技术文档提供了符合通用安全和性能要求的证据。"},
            # --- 2. 质量管理体系 (QA/QMS) ---
            {"module": "2. 质量管理体系 (QA)", "term": "CAPA", "cn": "纠正和预防措施", "context": "问题解决", "sentence": "A CAPA was opened to address the recurring calibration failure of the filling machine.", "sentence_cn": "已启动 CAPA 以解决灌装机反复出现的校准失败问题。"},
            {"module": "2. 质量管理体系 (QA)", "term": "Change Control", "cn": "变更控制", "context": "体系维持", "sentence": "Any modification to the manufacturing process requires a change control request.", "sentence_cn": "对生产工艺的任何修改都需要提交变更控制申请。"},
            {"module": "2. 质量管理体系 (QA)", "term": "Internal Audit", "cn": "内部审核", "context": "自查", "sentence": "The internal audit schedule covers all departments including R&D and Production.", "sentence_cn": "内审计划覆盖了包括研发和生产在内的所有部门。"},
            {"module": "2. 质量管理体系 (QA)", "term": "Non-conformity (NC)", "cn": "不合格", "context": "异常处理", "sentence": "The raw material was segregated due to a non-conformity in purity testing.", "sentence_cn": "由于纯度检测不合格，该原材料已被隔离。"},
            # --- 3. 设计与研发 (R&D) ---
            {"module": "3. 设计与研发 (R&D)", "term": "Design Input", "cn": "设计输入", "context": "开发初期", "sentence": "User needs are translated into technical design inputs.", "sentence_cn": "用户需求被转化为技术设计输入。"},
            {"module": "3. 设计与研发 (R&D)", "term": "Design Verification", "cn": "设计验证", "context": "输出vs输入", "sentence": "Design verification demonstrated that the device meets all specified requirements.", "sentence_cn": "设计验证表明该器械满足所有规定的要求。"},
            {"module": "3. 设计与研发 (R&D)", "term": "Formulation", "cn": "配方", "context": "试剂核心", "sentence": "The buffer formulation was optimized to improve the stability of the enzyme.", "sentence_cn": "缓冲液配方经过优化，以提高酶的稳定性。"},
            {"module": "3. 设计与研发 (R&D)", "term": "Scale-up", "cn": "工艺放大", "context": "转化阶段", "sentence": "The process scale-up from 1L to 50L was successfully validated.", "sentence_cn": "从 1L 到 50L 的工艺放大已成功验证。"},
            # --- 4. 生产与供应链 (Production) ---
            {"module": "4. 生产与供应链 (Ops)", "term": "Batch Record", "cn": "批记录", "context": "生产过程", "sentence": "The batch record must be reviewed and signed before product release.", "sentence_cn": "产品放行前必须审核并签署批记录。"},
            {"module": "4. 生产与供应链 (Ops)", "term": "Cold Chain", "cn": "冷链", "context": "运输/储存", "sentence": "Reagents must be transported under cold chain conditions (2-8°C).", "sentence_cn": "试剂必须在冷链条件（2-8°C）下运输。"},
            {"module": "4. 生产与供应链 (Ops)", "term": "Raw Material", "cn": "原材料", "context": "物料管理", "sentence": "Incoming raw materials are tested against specifications before acceptance.", "sentence_cn": "进厂原材料在接收前需对照规格进行测试。"},
            {"module": "4. 生产与供应链 (Ops)", "term": "Lot Number", "cn": "批号", "context": "追溯性", "sentence": "Traceability is maintained through the lot number printed on each vial.", "sentence_cn": "通过印在每个小瓶上的批号来维持可追溯性。"},
            # --- 5. 性能评价 (Performance) ---
            {"module": "5. 性能评价 (Performance)", "term": "LOD (Limit of Detection)", "cn": "检出限", "context": "灵敏度指标", "sentence": "The LOD of the assay is determined to be 0.5 ng/mL.", "sentence_cn": "该测定法的检出限确定为 0.5 ng/mL。"},
            {"module": "5. 性能评价 (Performance)", "term": "Interference", "cn": "干扰", "context": "特异性指标", "sentence": "Hemolysis interference was tested up to 500 mg/dL hemoglobin.", "sentence_cn": "溶血干扰测试至血红蛋白浓度 500 mg/dL。"},
            {"module": "5. 性能评价 (Performance)", "term": "Stability", "cn": "稳定性", "context": "效期", "sentence": "Real-time stability studies support a shelf life of 12 months.", "sentence_cn": "实时稳定性研究支持 12 个月的有效期。"},
            {"module": "5. 性能评价 (Performance)", "term": "Reference Range", "cn": "参考区间", "context": "临床解释", "sentence": "The reference range was established by testing 120 healthy individuals.", "sentence_cn": "参考区间是通过测试 120 名健康个体建立的。"},
            # --- 6. 风险管理 (Risk) ---
            {"module": "6. 风险管理 (Risk)", "term": "Hazard", "cn": "危险/危害源", "context": "风险源头", "sentence": "Biological contamination is a potential hazard for IVD reagents.", "sentence_cn": "生物污染是 IVD 试剂的潜在危害源。"},
            {"module": "6. 风险管理 (Risk)", "term": "Severity", "cn": "严重度", "context": "后果评估", "sentence": "The severity of the harm caused by false negative results is classified as critical.", "sentence_cn": "由假阴性结果造成的伤害严重度被归类为严重。"},
            {"module": "6. 风险管理 (Risk)", "term": "Residual Risk", "cn": "剩余风险", "context": "控制后", "sentence": "The residual risk is evaluated as acceptable after implementing risk controls.", "sentence_cn": "实施风险控制后，剩余风险被评估为可接受。"},
            # --- 7. 通用缩写 (Acronyms) ---
            {"module": "7. 通用缩写 (Acronyms)", "term": "UDI", "cn": "唯一器械标识", "context": "追溯", "sentence": "The UDI carrier must be readable on the label.", "sentence_cn": "标签上的 UDI 载体必须可读。"},
            {"module": "7. 通用缩写 (Acronyms)", "term": "PMS", "cn": "上市后监督", "context": "监控", "sentence": "The manufacturer shall maintain a PMS system to collect data on quality.", "sentence_cn": "制造商应维护上市后监督系统以收集质量数据。"},
            {"module": "7. 通用缩写 (Acronyms)", "term": "IFU", "cn": "使用说明书", "context": "文件", "sentence": "Please refer to the IFU for detailed operating instructions.", "sentence_cn": "请参阅使用说明书获取详细操作指南。"},
        ]
        # 写入 CSV
        df = pd.DataFrame(data)
        df.to_csv(CSV_FILE_PATH, index=False, encoding='utf-8')
        return True
    return False

# 检查并生成 CSV
newly_created = create_initial_csv()

# ==========================================
# 1. 核心逻辑：加载数据
# ==========================================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8', keep_default_na=False)
        return df
    except FileNotFoundError:
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ 读取文件出错: {e}")
        return pd.DataFrame()

df_all = load_data()

# ==========================================
# 2. 页面配置与初始化
# ==========================================
st.set_page_config(page_title="IVD Lingo Master", layout="wide", page_icon="🧬")

# 初始化 Session State
if 'current_card' not in st.session_state:
    st.session_state['current_card'] = None
if 'show_answer' not in st.session_state:
    st.session_state['show_answer'] = False

# 新增：用于存储选择题的选项和状态，防止刷新丢失
if 'mc_options' not in st.session_state:
    st.session_state['mc_options'] = [] # 存储当前的4个选项
if 'mc_answered' not in st.session_state:
    st.session_state['mc_answered'] = False # 标记是否已点击提交

def get_random_card(dataset):
    """从列表字典中随机抽取一张，并重置相关状态"""
    if not dataset:
        st.session_state['current_card'] = None
        return
    st.session_state['current_card'] = random.choice(dataset)
    st.session_state['show_answer'] = False

    # 重置选择题状态
    st.session_state['mc_options'] = []
    st.session_state['mc_answered'] = False

# ==========================================
# 3. 侧边栏 (Sidebar)
# ==========================================
st.sidebar.title("🧬 IVD 行业英语")

# 如果刚创建了文件，提示一下
if newly_created:
    st.sidebar.success(f"✅ 已自动生成演示数据文件: ivd_data.csv")

# 检查数据是否加载成功
if df_all.empty:
    st.error(f"❌ 数据文件为空或无法读取: {CSV_FILE_PATH}")
    st.stop()

# 1. 选择模块 (自动排序)
available_modules = sorted(df_all['module'].unique().tolist())
selected_module = st.sidebar.selectbox("选择学习模块", available_modules)

# 2. 模式选择 (增加了选择题模式)
learning_mode = st.sidebar.radio(
    "选择模式",
    ["📖 词汇表 (Dictionary)", "🃏 抽认卡 (Flashcards)", "📝 完形填空 (Quiz)", "🎯 选择题 (Multiple Choice)"]
)

# 3. 数据过滤
current_df = df_all[df_all['module'] == selected_module]
current_data = current_df.to_dict('records')

# ==========================================
# 4. 主界面逻辑
# ==========================================
st.title(f"{selected_module}")

# --- 模式 A: 词汇表 (Dictionary) ---
if learning_mode == "📖 词汇表 (Dictionary)":
    st.markdown("### 📚 核心词汇速查")

    # 动态列配置
    display_cols = ['term', 'cn', 'context']
    col_config = {
        "term": st.column_config.TextColumn("单词/缩写", help="IVD 行业专业术语"),
        "cn": "中文含义",
        "context": "行业语境"
    }

    # 检查是否有例句列
    if 'sentence' in current_df.columns:
        display_cols.extend(['sentence', 'sentence_cn'])
        col_config["sentence"] = "法规/行业例句 (En)"
        col_config["sentence_cn"] = "例句翻译 (Cn)"

    # 搜索功能
    search_term = st.text_input("🔍 搜索单词/中文:", "")
    if search_term:
        filtered_df = current_df[
            current_df['term'].str.contains(search_term, case=False, na=False) |
            current_df['cn'].str.contains(search_term, case=False, na=False)
        ]
    else:
        filtered_df = current_df

    st.caption(f"共找到 {len(filtered_df)} 个词汇")
    st.dataframe(
        filtered_df[display_cols],
        column_config=col_config,
        use_container_width=True,
        hide_index=True,
        height=600
    )

# --- 模式 B: 抽认卡 (Flashcards) ---
elif learning_mode == "🃏 抽认卡 (Flashcards)":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🧠 记忆训练")

        # 初始抽取或换组后重抽
        if (st.session_state['current_card'] is None or
            st.session_state['current_card'] not in current_data):
            get_random_card(current_data)

        card = st.session_state['current_card']

        if card:
            # 卡片容器
            card_container = st.container(border=True)
            with card_container:
                # 英文单词 (大号字体)
                st.markdown(f"<h1 style='text-align: center; color: #0068c9; margin-bottom: 20px;'>{card['term']}</h1>", unsafe_allow_html=True)

                if st.session_state['show_answer']:
                    st.markdown("---")
                    c_inner1, c_inner2 = st.columns([1, 2])
                    with c_inner1:
                        st.markdown(f"**中文:**")
                        st.markdown(f"### {card['cn']}")
                    with c_inner2:
                        st.info(f"🩺 **语境:** {card['context']}")

                    # 只有当例句不为空时才显示
                    if card.get('sentence'):
                        st.markdown("---")
                        st.warning(f"📜 **例句:** {card['sentence']}")
                        st.caption(f"🇨🇳 **翻译:** {card['sentence_cn']}")

            # 按钮区
            st.write("") # Spacer
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                if st.button("👀 查看答案", use_container_width=True):
                    st.session_state['show_answer'] = True
                    st.rerun()
            with b_col2:
                if st.button("⏭️ 下一个", use_container_width=True):
                    get_random_card(current_data)
                    st.rerun()
        else:
            st.warning("该模块暂无数据。")

# --- 模式 C: 完形填空 (Quiz) ---
elif learning_mode == "📝 完形填空 (Quiz)":
    st.markdown("### ✍️ 法规/标准例句填空")

    # 过滤掉没有例句的词
    quiz_data = [item for item in current_data if item.get('sentence')]

    if not quiz_data:
        st.warning("⚠️ 当前模块主要为术语缩写，无例句可供测试，请切换到词汇表或抽认卡模式。")
    else:
        # 如果当前卡片不在 quiz_data 里（比如刚从缩写切过来），重新抽
        if (st.session_state['current_card'] is None or
            st.session_state['current_card'] not in quiz_data):
            get_random_card(quiz_data)

        card = st.session_state['current_card']

        # 构造问题：不区分大小写替换
        term_to_hide = card['term']
        import re
        question_sentence = re.sub(re.escape(term_to_hide), "_______", card['sentence'], flags=re.IGNORECASE)

        st.markdown(f"**含义提示:** {card['cn']} ({card['context']})")
        st.markdown(f"#### {question_sentence}")

        with st.expander("🔍 需要提示？查看中文全句翻译"):
            st.caption(card['sentence_cn'])

        user_input = st.text_input("请输入缺失的单词:", key="quiz_input")

        c1, c2 = st.columns(2)
        if c1.button("提交答案", use_container_width=True):
            if user_input.strip().lower() == card['term'].lower():
                st.success("🎉 正确! (Correct)")
                st.markdown(f"**完整例句:** {card['sentence']}")
                st.caption(f"**翻译:** {card['sentence_cn']}") # 这里也可以顺手加一个
                st.balloons()
            else:
                st.error(f"❌ 错误. 正确答案是: **{card['term']}**")
                st.markdown(f"**完整例句:** {card['sentence']}")
                st.caption(f"**翻译:** {card['sentence_cn']}") # 这里也可以顺手加一个

        if c2.button("跳过/下一题", use_container_width=True):
            get_random_card(quiz_data)
            st.rerun()

# --- 模式 D: 选择题 (Multiple Choice) ---
elif learning_mode == "🎯 选择题 (Multiple Choice)":
    st.markdown("### 🎯 英译中选择测试")

    col_center, _ = st.columns([2, 1])

    # 1. 获取/初始化卡片
    if (st.session_state['current_card'] is None or
        st.session_state['current_card'] not in current_data):
        get_random_card(current_data)

    card = st.session_state['current_card']

    if card:
        with col_center:
            # 2. 生成选项逻辑 (仅在没有生成过选项时执行，防止刷新页面时选项变动)
            if not st.session_state['mc_options']:
                correct_answer = card['cn']
                # 获取所有其他可能的中文含义作为干扰项
                all_meanings = list(set([item['cn'] for item in df_all.to_dict('records') if item['cn'] != correct_answer]))

                # 如果干扰项不够3个，就取全部
                if len(all_meanings) < 3:
                    distractors = all_meanings
                else:
                    distractors = random.sample(all_meanings, 3)

                options = distractors + [correct_answer]
                random.shuffle(options)
                st.session_state['mc_options'] = options

            # 3. 显示题目
            st.markdown(f"请选择单词 **:blue[{card['term']}]** 的正确含义：")

            # 4. 显示单选框
            # 使用 key 保存用户的选择，避免刷新丢失
            user_choice = st.radio("Options:", st.session_state['mc_options'], label_visibility="collapsed")

            # 5. 提交按钮逻辑
            c_check, c_next = st.columns([1, 1])

            with c_check:
                if st.button("✅ 提交", use_container_width=True, disabled=st.session_state['mc_answered']):
                    st.session_state['mc_answered'] = True
                    if user_choice == card['cn']:
                        st.success("🎉 回答正确！")
                        st.balloons()
                    else:
                        st.error(f"❌ 回答错误。正确答案是：{card['cn']}")

            with c_next:
                if st.button("⏭️ 下一题", use_container_width=True):
                    get_random_card(current_data)
                    st.rerun()

            # 提交后显示额外信息
            if st.session_state['mc_answered']:
                with st.expander("查看详细信息", expanded=True):
                    st.info(f"**语境:** {card['context']}")
                    if card.get('sentence'):
                        st.markdown(f"**例句:** {card['sentence']}")
                        st.caption(f"**翻译:** {card['sentence_cn']}") # <--- 增加了这行中文翻译
    else:
        st.warning("该模块数据不足，无法生成测试。")

st.sidebar.markdown("---")
st.sidebar.caption(f"Data Source: {os.path.basename(CSV_FILE_PATH)}")