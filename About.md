## Inspiration

Our team has always been fascinated by the potential of AI to enhance learning and simplify everyday tasks. We envision a future where AI seamlessly supports us in understanding complex information and planning even complicated endeavors like travel. This project represents an exciting step towards realizing that vision.

## What it does

Our project merges two core functionalities:

* **AI Teacher:** This component empowers users to create searchable knowledge bases from textual information. You can upload `.txt` files or record your own text, and the AI-Teacher generates embeddings to enable understanding and efficient retrieval of the knowledge within.

* **Natural Language Flight Finder:** This element offers a conversational approach to travel planning. Instead of wrestling with traditional booking platforms, users can find flights through simple language interaction (e.g., "Show me round-trip flights from Chicago to London for November.").

## How we built it

* **Gemini API:** Google's powerful LLM forms the backbone of our project, driving text understanding, embedding creation, and knowledge query responses.
* **ChromaDB:** Provides a robust database solution optimized for storing and managing the embeddings generated for the AI Teacher. 
* **OpenAI API:** Underpins our flight finder, enabling it to interpret natural language requests and pinpoint relevant flight options.
* **Web Interface:** Provides an intuitive interface for users to interact with both project components. We integrated frontend and backend systems with technologies like Flask for dynamic communication.

## Challenges we ran into

* **Seamless integration:** Ensuring smooth communication and efficient interplay  between the AI Teacher and Flight Finder, driven by diverse AI APIs, posed a significant challenge. 
* **Scalability:** Designing a system that can gracefully handle growing knowledge bases and increasing search complexity with the AI Teacher.
* **Refining Natural Language Understanding:** Fine-tuning the Flight Finder's interpretation of conversational travel requests required significant  iteration and testing.

## Accomplishments that we're proud of

* **User-Centric Knowledge Management:** Enabling users to build and personalize their own knowledge repositories with the AI Teacher.
* **Intuitive Travel Planning:** Simplifying the often-frustrating process of flight booking through conversational search.
* **Successful AI Integration:**  Demonstrating the potential for combining multiple cutting-edge AI technologies to provide tangible benefits.

## What we learned

* **The Power of Embeddings:** The use of embeddings to represent text semantically offers great potential for personalized knowledge representation.
* **The Importance of Nuanced AI Interaction:** Designing user-friendly and effective interactions with AI models is crucial for practical applications. 
* **Real-World AI Challenges:** Integrating and scaling a project of this kind goes far beyond simple prototypes, highlighting practical issues of engineering and deployment.

## What's next for AI Agents

We're keen to explore:

* **Multimodal Input:** Extending the AI Teacher to ingest images, diagrams, and  other non-textual  knowledge sources.
* **Integrating Flight Reservations:** Adding flight booking capabilities directly within the Flight Finder to create a comprehensive travel solution.
* **Enhanced Personalization:** Leveraging additional user data to provide even more tailored learning experiences and travel recommendations.
