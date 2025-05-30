from transformers import GPT2Tokenizer

# 加载GPT-2分词器
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-xl')

# 解码单个token
token_id = 1234  # 您要解码的token
decoded_text = tokenizer.decode([token_id])
print(f"Token {token_id}: '{decoded_text}'")

# 解码多个token
token_ids = [50256,   317,  2196,   286, 18426,   262, 41078, 31897,   373,  4166,
          416, 13406,   290,  2716,   287, 10249,   329,   262, 29490, 18993,
           13,   632,   373,   262,   717,   983,   287,   262, 18426,   262,
        41078, 31897,  8663,   284,   307,  2716,   319,   257,  1363,  8624,
           13,   198,   198, 15842,   905,    60,   198,   198, 43241,   198,
          198,    50,  9229,   262, 41078, 31897,   318,   257,  1735,    12,
         1416, 18886,  3859,   983,   287,   543,   262,  2137,  6973, 18426,
           11,   257,  4171, 19859, 31897,    11,   290,   465,  2460,    11,
          309,  1768,    11,  6102, 34083,    11,   290, 14235,  8049,    13,
          383,  2137,  6973, 18426,   290,   465,  2460,   355,   484,  3067,
          832,   257,  2168,   286,  9539,    11,  1123,   351,   257,  1180,
         7505,    13,   198,   198,   464,  2137,  6973, 18426,   290,   465,
         2460,   355,   484,  3067,   832,   257,  2168,   286,  9539,    11,
         1123,   351,   257,  1180,  7505,    13,   198,   198, 11605,   198,
          198,    50,  9229,   262, 41078, 31897,   318,   257,  1735,    12,
         1416, 18886,  3859,   983,   287,   543,   262,  2137,  6973, 18426,
           11,   257,  4171, 19859, 31897,    11,   290,   465,  2460,    11,
          309,  1768,    11,  6102, 34083,    11,   290, 14235,  8049,    13,
          383,  2137,  6973, 18426,   290,   465,  2460,   355,   484,  3067,
          832,   257,  2168,   286,  9539,    11,  1123,   351,   257,  1180,
         7505,    13,   198,   198,   464,  2137,  6973, 18426,   290,   465,
         2460,   355,   484,  3067,   832,   257,  2168,   286,  9539,    11,
         1123,   351,   257,  1180,  7505,    13,   198,   198, 43241,   198,
          198,    50,  9229,   262, 41078, 31897,   318,   257,  1735,    12,
         1416, 18886,  3859,   983,   287,   543,   262,  2137,  6973, 18426,
           11,   257,  4171, 19859, 31897,    11,   290,   465,  2460,    11,
          309,  1768,    11,  6102, 34083,    11,   290, 14235,  8049,    13,
          383,  2137]  # 您要解码的token列表
decoded_text = tokenizer.decode(token_ids)
print("*"*50)
print(f"decoded_text: '{decoded_text}'")

# 查看词汇表大小
print(f"词汇表大小: {len(tokenizer)}")  # 应该是50257