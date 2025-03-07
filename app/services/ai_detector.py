import openai
import re
from config import config

openai.api_key = config.OPENAI_API_KEY

prompt= """
### **Objective:**  
Analyze the given text and assess whether it was generated by AI or written by a human. Focus on subtle patterns, inconsistencies, and specific AI-related behaviors in the text.

### **Key Detection Factors:**  

1. **Linguistic Patterns & Repetitiveness**  
   - Look for unnatural sentence structures and excessive use of common phrases or connectors (e.g., "in conclusion," "it is important to note").  
   - Detect redundant phrases or ideas repeated in different forms, a sign of AI-generated content.  

2. **Contextual Awareness & Deep Reasoning**  
   - Assess if the text exhibits shallow understanding or lacks depth. AI often generates factual yet superficial statements that don’t align with complex, real-world reasoning.  
   - Check for lack of personal anecdotes, specific life experiences, or logical flaws that are typical of AI.  

3. **Coherence and Flow**  
   - Examine the logical flow between sentences and paragraphs. AI-generated text may appear disjointed or lose coherence over longer passages.  
   - Look for abrupt transitions or overuse of transitional phrases that are typical of AI's attempt to maintain fluidity.  

4. **Factual Accuracy & Inconsistencies**  
   - Analyze for over-precision or unnecessary accuracy, where the text might present facts with an unnatural certainty or lack of context.  
   - Detect any contradictions, factual inconsistencies, or oddly generic statements that are typical of AI text generation.  

5. **Human-Like Nuance, Emotion, & Imperfections**  
   - Examine whether the text includes personal experiences, humor, emotional depth, or subjective views.  
   - Identify if the text seems overly neutral, objective, or lacks human imperfections (e.g., typos, minor logical errors, conversational flow).  

6. **Predictability & Structure**  
   - Detect rigid sentence structures or overly polished, formal tone. AI often generates text that feels structured or organized in a way that’s too predictable.  
   - Evaluate the overall tone for any signs of forced neutrality or lack of personal voice.  

### **Output:**  
Return only a **confidence score** between **0-100%**, where 0% indicates human-written and 100% indicates AI-generated.  

### **Example Output:**  
`87% AI-generated`  
`13% Human-written`  

**Be rigorous in identifying even the most subtle signs of AI generation.** The text may be grammatically correct, but inconsistencies in context, depth, and emotional authenticity should be carefully considered.

"""

class AIDetector:
    @staticmethod
    async def detect_ai_text(text: str) -> int:
        """Detect AI-generated text and return a confidence percentage."""
        response =  openai.chat.completions.create(
            model="gpt-4o-mini",
            temperature = 1,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ],
        )
        result = response.choices[0].message.content
        print(result)

        # Extract percentage using regex
        match = re.search(r"\b(\d{1,3})\b", result)
        return int(match.group(1)) if match else 0
