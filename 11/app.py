import streamlit as st
import time
import random

quotes = [
    {"Number": 1, "Quote Topic": "Stages of Life 🌱", "Quote": "Every age unfolds a new lesson. Life's chapters evolve, each teaching us anew."},
    {"Number": 2, "Quote Topic": "Stages of Life 🌱", "Quote": "From infancy to twilight, our journey is painted in growth. Every stage shines with its own wisdom."},
    {"Number": 3, "Quote Topic": "Identity 🎭", "Quote": "We piece together our identity with experiences. In the vast cosmos, our ever-changing signature is our identity."},
    {"Number": 4, "Quote Topic": "Identity 🎭", "Quote": "We aren't born with a defined self. Our identity is an art, crafted through introspection and encounters."},
    {"Number": 5, "Quote Topic": "Enlightenment 💡", "Quote": "Every step towards enlightenment is a dive within. It's an ongoing journey of self and universe."},
    {"Number": 6, "Quote Topic": "Enlightenment 💡", "Quote": "True insight isn't just about knowledge. It's the harmony of mind, heart, and soul."},
    {"Number": 7, "Quote Topic": "Adaptive Resonance Theory 🧠", "Quote": "Our cognition is like a river, ever-flowing and adapting. Every experience shapes its course, forming new resonances."},
    {"Number": 8, "Quote Topic": "Adaptive Resonance Theory 🧠", "Quote": "The brain's capacity to learn is profound. It finds its rhythm in adaptive resonances."},
    {"Number": 9, "Quote Topic": "Panpsychism 🌌", "Quote": "The universe might hum with consciousness in every atom. Every speck could be part of this grand song."},
    {"Number": 10, "Quote Topic": "Panpsychism 🌌", "Quote": "What if consciousness isn't exclusive to us? The universe's shared melody might be sung by all."},
    {"Number": 11, "Quote Topic": "How to Think 🤔", "Quote": "Thinking isn't about arriving, it's about exploring. Dive deep, question, and embrace the universe within."},
    {"Number": 12, "Quote Topic": "How to Think 🤔", "Quote": "To think profoundly is to touch the cosmos. It's about connecting with the vastness and intricacies it holds."},
    {"Number": 13, "Quote Topic": "Plants Communication 🌿", "Quote": "In every leaf and root, plants tell tales of life. Their silent growth is a language we're just beginning to decipher."},
    {"Number": 14, "Quote Topic": "Plants Communication 🌿", "Quote": "Nature's every rustle is a whispered secret. It's a testament to the intricate web of communication."},
    {"Number": 15, "Quote Topic": "Fame 🌟", "Quote": "True impact outlives fleeting fame. What endures is the legacy we craft, not the applause we receive."},
    {"Number": 16, "Quote Topic": "Fame 🌟", "Quote": "Fame might shine bright, but it's transient. Genuine influence is the silent footprint we leave in time."},
    {"Number": 17, "Quote Topic": "Happiness 😊", "Quote": "True happiness is an inner light that shines brightest in shared moments."},
    {"Number": 18, "Quote Topic": "Happiness 😊", "Quote": "Life's riches aren't material but the joyous moments and heartfelt memories we gather."},
    {"Number": 19, "Quote Topic": "Exercise 🏃", "Quote": "Exercise is the symphony of the body, resonating with health and vitality."},
    {"Number": 20, "Quote Topic": "Exercise 🏃", "Quote": "In movement, we find balance, strength, and a celebration of life's potential."},
    {"Number": 21, "Quote Topic": "Good Habits 🔄", "Quote": "Good habits are the bricks that build the mansion of success."},
    {"Number": 22, "Quote Topic": "Good Habits 🔄", "Quote": "Consistency in habits crafts our destiny, one action at a time."},
    {"Number": 23, "Quote Topic": "Discipline 🕰️", "Quote": "Discipline is the bridge between dreams and their realization."},
    {"Number": 24, "Quote Topic": "Discipline 🕰️", "Quote": "Through discipline, chaos transforms into order, and aspirations into achievements."},
    {"Number": 25, "Quote Topic": "Stamina 🚀", "Quote": "Stamina isn't just enduring but thriving amidst challenges."},
    {"Number": 26, "Quote Topic": "Stamina 🚀", "Quote": "It's stamina that turns obstacles into stepping stones, fueling our journey forward."},
    {"Number": 27, "Quote Topic": "Artificial General Intelligence 🤯", "Quote": "AGI is not just about mimicking humans but understanding the core of intelligence itself."},
    {"Number": 28, "Quote Topic": "Artificial General Intelligence 🤯", "Quote": "The pursuit of AGI is a testament to humanity's quest to transcend its own boundaries."},
    {"Number": 29, "Quote Topic": "AI Pipelines 🛠️", "Quote": "AI pipelines are the arteries of intelligent systems, directing the flow of knowledge."},
    {"Number": 30, "Quote Topic": "AI Pipelines 🛠️", "Quote": "In well-crafted pipelines, AI finds its rhythm, efficiency, and transformative power."},
    {"Number": 31, "Quote Topic": "Genius 🌟", "Quote": "Genius isn't just raw talent; it's the alchemy of persistence, passion, and perspective."},
    {"Number": 32, "Quote Topic": "Genius 🌟", "Quote": "Every spark of genius has been nurtured by curiosity and an insatiable thirst for knowledge."},
    {"Number": 33, "Quote Topic": "Our Brains 🧠", "Quote": "Our brain is the universe's masterpiece, a nexus of thoughts, dreams, and memories."},
    {"Number": 34, "Quote Topic": "Our Brains 🧠", "Quote": "In every neuron, our brain holds the potential of countless possibilities and imaginations."},
    {"Number": 35, "Quote Topic": "Our Brains 🧠", "Quote": "The intricacies of our brain reflect the cosmos: vast, complex, and beautifully mysterious."},
    {"Number": 36, "Quote Topic": "Our Brains 🧠", "Quote": "Understanding our brain is the key to unlocking the enigmas of consciousness, behavior, and potential."},
    {"Number": 37, "Quote Topic": "Mindfulness 🌼", "Quote": "Mindfulness is the anchor that grounds us in the present, amidst life's tumultuous seas."},
    {"Number": 38, "Quote Topic": "Mindfulness 🌼", "Quote": "In the act of being mindful, we embrace life's symphony, note by note, moment by moment."},
    {"Number": 39, "Quote Topic": "Resilience 💪", "Quote": "Resilience is the art of bouncing back, turning wounds into wisdom and setbacks into comebacks."},
    {"Number": 40, "Quote Topic": "Resilience 💪", "Quote": "Life will test us, but with resilience, we rise, stronger and more enlightened."},
    {"Number": 41, "Quote Topic": "Innovation 💡", "Quote": "Innovation is the heartbeat of progress, pushing boundaries and redefining possibilities."},
    {"Number": 42, "Quote Topic": "Innovation 💡", "Quote": "Every breakthrough, every invention, is a testament to humanity's relentless spirit of innovation."},
    {"Number": 43, "Quote Topic": "Empathy ❤️", "Quote": "Empathy is the bridge between souls, transcending words and touching hearts."},
    {"Number": 44, "Quote Topic": "Empathy ❤️", "Quote": "Through empathy, we see the world through another's eyes, fostering understanding and unity."},
    {"Number": 45, "Quote Topic": "Happiness 😊", "Quote": "True happiness is an inner light that shines brightest in shared moments."},
    {"Number": 46, "Quote Topic": "Happiness 😊", "Quote": "Life's riches aren't material but the joyous moments and heartfelt memories we gather."},
    {"Number": 47, "Quote Topic": "Exercise 🏃", "Quote": "Exercise is the symphony of the body, resonating with health and vitality."},
    {"Number": 48, "Quote Topic": "Exercise 🏃", "Quote": "In movement, we find balance, strength, and a celebration of life's potential."},
    {"Number": 49, "Quote Topic": "Good Habits 🔄", "Quote": "Good habits are the bricks that build the mansion of success."},
    {"Number": 50, "Quote Topic": "Good Habits 🔄", "Quote": "Consistency in habits crafts our destiny, one action at a time."},
    {"Number": 51, "Quote Topic": "Discipline 🕰️", "Quote": "Discipline is the bridge between dreams and their realization."},
    {"Number": 52, "Quote Topic": "Discipline 🕰️", "Quote": "Through discipline, chaos transforms into order, and aspirations into achievements."},
    {"Number": 53, "Quote Topic": "Stamina 🚀", "Quote": "Stamina isn't just enduring but thriving amidst challenges."},
    {"Number": 54, "Quote Topic": "Stamina 🚀", "Quote": "It's stamina that turns obstacles into stepping stones, fueling our journey forward."},
    {"Number": 55, "Quote Topic": "Artificial General Intelligence 🤯", "Quote": "AGI is not just about mimicking humans but understanding the core of intelligence itself."},
    {"Number": 56, "Quote Topic": "Artificial General Intelligence 🤯", "Quote": "The pursuit of AGI is a testament to humanity's quest to transcend its own boundaries."},
    {"Number": 57, "Quote Topic": "AI Pipelines 🛠️", "Quote": "AI pipelines are the arteries of intelligent systems, directing the flow of knowledge."},
    {"Number": 58, "Quote Topic": "AI Pipelines 🛠️", "Quote": "In well-crafted pipelines, AI finds its rhythm, efficiency, and transformative power."},
    {"Number": 59, "Quote Topic": "Genius 🌟", "Quote": "Genius isn't just raw talent; it's the alchemy of persistence, passion, and perspective."},
    {"Number": 60, "Quote Topic": "Genius 🌟", "Quote": "Every spark of genius has been nurtured by curiosity and an insatiable thirst for knowledge."},
    {"Number": 61, "Quote Topic": "Our Brains 🧠", "Quote": "Our brain is the universe's masterpiece, a nexus of thoughts, dreams, and memories."},
    {"Number": 62, "Quote Topic": "Our Brains 🧠", "Quote": "In every neuron, our brain holds the potential of countless possibilities and imaginations."},
    {"Number": 63, "Quote Topic": "Our Brains 🧠", "Quote": "The intricacies of our brain reflect the cosmos: vast, complex, and beautifully mysterious."},
    {"Number": 64, "Quote Topic": "Our Brains 🧠", "Quote": "Understanding our brain is the key to unlocking the enigmas of consciousness, behavior, and potential."},
    {"Number": 65, "Quote Topic": "Mindfulness 🌼", "Quote": "Mindfulness is the anchor that grounds us in the present, amidst life's tumultuous seas."},
    {"Number": 66, "Quote Topic": "Mindfulness 🌼", "Quote": "In the act of being mindful, we embrace life's symphony, note by note, moment by moment."},
    {"Number": 67, "Quote Topic": "Resilience 💪", "Quote": "Resilience is the art of bouncing back, turning wounds into wisdom and setbacks into comebacks."},
    {"Number": 68, "Quote Topic": "Resilience 💪", "Quote": "Life will test us, but with resilience, we rise, stronger and more enlightened."},
    {"Number": 69, "Quote Topic": "Innovation 💡", "Quote": "Innovation is the heartbeat of progress, pushing boundaries and redefining possibilities."},
    {"Number": 70, "Quote Topic": "Innovation 💡", "Quote": "Every breakthrough, every invention, is a testament to humanity's relentless spirit of innovation."},
    {"Number": 71, "Quote Topic": "Empathy ❤️", "Quote": "Empathy is the bridge between souls, transcending words and touching hearts."},
    {"Number": 72, "Quote Topic": "Empathy ❤️", "Quote": "Through empathy, we see the world through another's eyes, fostering understanding and unity."},
    {"Number": 73, "Quote Topic": "Inspiration 🌈", "Quote": "Inspiration is the spark that ignites the soul, propelling us to chase our dreams."},
    {"Number": 74, "Quote Topic": "Inspiration 🌈", "Quote": "Every moment of inspiration is a call to action, pushing us beyond our boundaries."},
    {"Number": 75, "Quote Topic": "Learning 📚", "Quote": "Learning is the gateway to growth, opening doors to endless possibilities."},
    {"Number": 76, "Quote Topic": "Learning 📚", "Quote": "Every lesson learned is a step towards enlightenment, broadening our horizons."},
    {"Number": 77, "Quote Topic": "Collaboration 🤝", "Quote": "In collaboration, we find strength. Together, we achieve more than we could alone."},
    {"Number": 78, "Quote Topic": "Collaboration 🤝", "Quote": "Unity in purpose paves the way for monumental achievements, showcasing the power of collective effort."},
    {"Number": 79, "Quote Topic": "Dreams 🌌", "Quote": "Dreams are the architects of our future. They sketch the blueprint of our aspirations."},
    {"Number": 80, "Quote Topic": "Dreams 🌌", "Quote": "In dreams, we find hope, and with hope, we transform the fabric of reality."},
    {"Number": 81, "Quote Topic": "Courage 🦁", "Quote": "Courage is the fire that lights our path, even in the face of overwhelming odds."},
    {"Number": 82, "Quote Topic": "Courage 🦁", "Quote": "With courage in our hearts, we defy limitations and embrace the vastness of potential."},
    {"Number": 83, "Quote Topic": "Change 🌀", "Quote": "Change is life's only constant. It shapes, molds, and propels us forward."},
    {"Number": 84, "Quote Topic": "Change 🌀", "Quote": "Embracing change is embracing growth, an acknowledgment of life's ever-evolving nature."},
    {"Number": 85, "Quote Topic": "Adventure 🌍", "Quote": "Life is an adventure, filled with twists, turns, and unexpected discoveries."},
    {"Number": 86, "Quote Topic": "Adventure 🌍", "Quote": "Every adventure, big or small, adds a chapter to our story, enriching our experience."},
    {"Number": 87, "Quote Topic": "Creativity 🎨", "Quote": "Creativity is the dance of the soul, expressing itself in countless forms."},
    {"Number": 88, "Quote Topic": "Creativity 🎨", "Quote": "Through creativity, we paint the world in vibrant colors, showcasing our unique perspectives."},
    {"Number": 89, "Quote Topic": "Passion ❤️", "Quote": "Passion is the fuel for our journey, driving us to chase after our dreams."},
    {"Number": 90, "Quote Topic": "Passion ❤️", "Quote": "With passion, every task becomes a labor of love, and every challenge, a thrilling endeavor."},
    {"Number": 91, "Quote Topic": "Hope 🌟", "Quote": "Hope is the beacon that guides us through stormy nights, reminding us of the dawn that awaits."},
    {"Number": 92, "Quote Topic": "Hope 🌟", "Quote": "In hope, we find solace, and in its embrace, we find the strength to persevere."},
    {"Number": 93, "Quote Topic": "Intuition 🧭", "Quote": "Intuition is the silent whisper of the soul, guiding us with its subtle wisdom."},
    {"Number": 94, "Quote Topic": "Intuition 🧭", "Quote": "By tuning into our intuition, we align with our inner compass, navigating life with clarity."},
    {"Number": 95, "Quote Topic": "Joy 😃", "Quote": "Joy is the melody of the heart, a song of gratitude and love."},
    {"Number": 96, "Quote Topic": "Joy 😃", "Quote": "In moments of joy, we connect with the essence of life, celebrating its beauty."},
    {"Number": 97, "Quote Topic": "Wisdom 🦉", "Quote": "Wisdom is the culmination of experience, a treasure trove of insights and reflections."},
    {"Number": 98, "Quote Topic": "Wisdom 🦉", "Quote": "With wisdom, we navigate life's complexities, drawing from the lessons of the past."},
    {"Number": 99, "Quote Topic": "Love ❤️", "Quote": "Love is the universal language, transcending boundaries and touching souls."},
    {"Number": 100, "Quote Topic": "Love ❤️", "Quote": "Through love, we find connection, unity, and the essence of existence."}
]

def display_quote(index):
    '''Function to display the quote using st.markdown()'''
    number = quotes[index]['Number']
    topic = quotes[index]['Quote Topic']
    quote = quotes[index]['Quote']
    st.markdown(f"### {number}. {topic}")
    st.markdown(quote)

# Streamlit app
def main():

    # Session state to hold the value of AutoRepeat button across reruns
    if "auto_repeat" not in st.session_state:
        st.session_state.auto_repeat = "On"
    if "current_index" not in st.session_state:
        st.session_state.current_index = random.randint(0, len(quotes)-1)

    st.title("Quote Bot AutoRepeater")

    # AutoRepeat radio button
    st.session_state.auto_repeat = st.radio("🔄 AutoRepeat", ["On", "Off"], horizontal=True)

    # Display the current quote
    display_quote(st.session_state.current_index)

    # Timer logic
    if st.session_state.auto_repeat == "On":
        timer_placeholder = st.empty()
        for i in range(10, 0, -1):
            timer_placeholder.text(f"Time left: {i} seconds")
            time.sleep(1)
            if i == 1:
                st.session_state.current_index = random.randint(0, len(quotes)-1)
                st.experimental_rerun()

if __name__ == "__main__":
    main()
