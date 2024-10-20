from sglang import function, system, user, assistant, gen, set_default_backend, RuntimeEndpoint

@function
def multi_turn_question(s):
    s += system("A is a pirate chatbot who always responds in pirate speak. B is a friendly chatbot who always responds in an amiable speak.")
    s += system("You are A.")
    s += system("You are B.")
    intro='''
Please give me an introduction of yourself.
To write a detailed introduction of yourself, follow these steps to ensure your introduction is engaging, informative, and well-structured. Think of it as telling your story in a way that gives the reader a clear sense of who you are, your background, and what you value.

### Step 1: Begin with Basic Information
Start with your full name, where you're from, and any relevant personal background that helps the reader know the basics about you.

- **Example**:  
  "Hello, my name is Sarah Mitchell. I was born and raised in Austin, Texas, a city known for its vibrant culture and live music scene. Growing up in such a creative environment has had a huge influence on my personality and career path."

### Step 2: Highlight Educational Background
Provide a summary of your educational journey. Include degrees, schools attended, and any notable achievements or areas of study.

- **Example**:  
  "I graduated with a Bachelor of Science in Computer Engineering from the University of Texas, where I also took part in several extracurricular activities, such as the Robotics Club and Student Government."

### Step 3: Describe Your Professional Experience or Career
Talk about your career or professional journey. Mention your current role, key responsibilities, and any significant past roles or experiences that shaped your career.

- **Example**:  
  "Currently, I work as a software developer at Tech Innovators, where I specialize in creating efficient, user-friendly mobile applications. Before joining Tech Innovators, I spent two years working as a junior developer at XYZ Corp, gaining invaluable experience in backend development and project management."

### Step 4: Share Personal Interests and Passions
Include your hobbies, interests, and passions outside of work or school. This helps give a sense of who you are as a person, beyond your professional or academic achievements.

- **Example**:  
  "Outside of work, I am an avid reader, particularly of science fiction and fantasy. I also enjoy hiking and have completed several long-distance treks in national parks across the U.S. In my free time, I love working on personal coding projects or volunteering at local animal shelters."

### Step 5: Discuss Future Goals or Aspirations
Explain what you're working toward or what your future ambitions are. This could include professional goals, personal development objectives, or a vision for the future.

- **Example**:  
  "In the future, I hope to advance into a leadership role within the tech industry, guiding a team of developers to innovate and create cutting-edge technologies. Additionally, I aim to continue expanding my knowledge of artificial intelligence and machine learning."

### Step 6: End with a Personal Touch or Invitation
Close with a friendly statement that invites connection or leaves a memorable final impression.

- **Example**:  
  "I'm always excited to meet new people and exchange ideas, so feel free to reach out if you'd like to connect. Whether it's discussing the latest in tech or finding new hiking trails, I'm happy to chat!"

### Full Example of a Self-Introduction:

"Hello, my name is Sarah Mitchell. I was born and raised in Austin, Texas, a city known for its vibrant culture and live music scene. Growing up in such a creative environment has had a huge influence on my personality and career path.

I graduated with a Bachelor of Science in Computer Engineering from the University of Texas, where I also took part in several extracurricular activities, such as the Robotics Club and Student Government. Currently, I work as a software developer at Tech Innovators, where I specialize in creating efficient, user-friendly mobile applications. Before joining Tech Innovators, I spent two years working as a junior developer at XYZ Corp, gaining invaluable experience in backend development and project management.

Outside of work, I am an avid reader, particularly of science fiction and fantasy. I also enjoy hiking and have completed several long-distance treks in national parks across the U.S. In my free time, I love working on personal coding projects or volunteering at local animal shelters.

In the future, I hope to advance into a leadership role within the tech industry, guiding a team of developers to innovate and create cutting-edge technologies. Additionally, I aim to continue expanding my knowledge of artificial intelligence and machine learning.

I'm always excited to meet new people and exchange ideas, so feel free to reach out if you'd like to connect. Whether it's discussing the latest in tech or finding new hiking trails, I'm happy to chat!"

By following these steps, you create a comprehensive and engaging self-introduction that covers key areas of your life while also showing personality and individuality. 
                    '''
    s+=user(intro)
    forks = s.fork(2)
    forks[0] += assistant(gen("introduction",ignore=["You are A."]))
    forks[1] += assistant(gen("introduction",ignore=["You are B."]))
    forks.join()
    # s += user(question_1)
    # s += assistant(gen("answer_1", max_tokens=256))
    # s += user(question_2)
    # forks = s.fork(2)
    # for i, f in enumerate(forks):
    #     f += f"The {i+1} one is:\n"
    #     f += gen(f"attractions")
    #     # print(f)
    # s += assistant(forks[0]["attractions"] + "\n")
    # s += user("test")
    # s += assistant(forks[1]["attractions"] + "\n")

set_default_backend(RuntimeEndpoint("http://localhost:30000"))

state = multi_turn_question.run(
    # question_1="What is the capital of the United States?",
    # question_2="List two local attractions.",
)

print(state["introduction"])
# for m in state.messages():
#     print(m["role"], ":", m["content"])

#print(state["answer_1"])