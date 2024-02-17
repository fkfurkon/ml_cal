from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/foodselection', methods=['POST'])
def Submit():
    global FoodType, Clean, Halal, Taste
    # new_image_path = 'Img_0.jpg'
    # image_viewer.object = new_image_path
    # console.log(food_type.value, calories.value, flavor.value, country.value, clean.value, halal.value)
    FoodType = request.form['food-type']
    calories = request.form['calories']
    Taste = request.form['flavor']
    country = request.form['country']
    Clean = request.form.get('clean-food') == 'on'
    Halal = request.form.get('halal-food') == 'on'
    
    print(FoodType, calories, Taste, country, Clean, Halal)

    main_ai()
    image_url = "/static/Img_0.jpg"
    return render_template('index.html', image_url=image_url)

# open ai
import openai
from base64 import b64decode
import openai
from googletrans import Translator

openai.api_key = "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"
model_1 = "ft:gpt-3.5-turbo-0613:personal:chatner-bot:8rLa33uZ"
model_2 = "ft:gpt-3.5-turbo-0613:personal:chatner-bot:8rsOdHmF"

FoodType = "เครื่องดื่ม" #ของหวาน เครื่องดื่ม อาหารทั่วไป
FoodCountry = "ญี่ปุ่น"  #อเมริกา อิตาลี โปรตุเกส ญี่ปุ่น ฝรั่งเศส เยอรมณี อินเดีย เกาหลี ไทย
Clean = False
Halal = False
Taste = "หวาน" #เค็ม หวาน เปรี้ยว เผ็ด ครีมมี่
Calories = "100"#10 20 50 100 200 240 250 integer

def check_attribute(attribute):
    return "ไม่" if not attribute else ""

Clean_result = check_attribute(Clean)
Halal_result = check_attribute(Halal)

def generate_chat_response(model_id, messages, temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response["choices"][0]["message"]["content"]


def generateImage_AndSave(prompt , image_count) :
    images = []
    response = openai.Image.create(
        prompt = prompt , 
        n = image_count , 
        size = '1024x1024' , 
        response_format = 'b64_json')
    
    for image in response['data'] :
        images.append(image.b64_json)

    prefix = 'Img'
    for index,image in enumerate(images):
        with open(f'{prefix}_{index}.jpg' ,'wb') as file :
            file.write(b64decode(image))

def translate_thai_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='th', dest='en')
    return translation.text

def main_ai():
    fine_tuned_model_id = model_2
    system_message = "คุณคือหุ่นยนต์แชทบอทสำหรับการตอบคำถามด้านอาหารโดยเฉพาะ"
    user_message = f'อยากกินอาหาร ประเภท {FoodType} ประเทศ{FoodCountry} {Clean_result}อาหารคลีน {Halal_result}ฮาลาล  รส{Taste} {Calories} แคล'
    test_messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response_content = generate_chat_response(
        model_id=fine_tuned_model_id,
        messages=test_messages
    )

    print("คำสั่ง : " , user_message)
    print("อาหารที่แนะนำคือ : " , response_content)

    print("Generating image . . . . ")
    
    english_translation = translate_thai_to_english(response_content)
    print("English translation => " , english_translation)
    generateImage_AndSave(f'{english_translation} + 1 piece + placed on the table' , image_count=1)

    print("Generated Image Done !!")
# open ai -------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
