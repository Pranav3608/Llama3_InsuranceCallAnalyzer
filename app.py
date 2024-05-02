import gradio as gr
from src.processing import process_transcript, extract_metadata_from_transcript

def analyze_transcript(transcript):
    # defining the schema points againts which verification or compliance checks have to be made
    schema = {
    "Introduction and Establishing Rapport": "The conversation starts with the agent introducing herself and expressing readiness to assist, establishing a rapport.",
    "Gathering Initial Information": "The agent inquires about the client's financial situation and specific concerns related to life insurance, to which the client provides relevant details.",
    "Explanation of Life Insurance Types": "The agent explains the two main types of life insurance, providing recommendations based on the client's circumstances.",
    "Determining Coverage Amount": "The agent discusses the needs analysis process to determine the appropriate coverage amount, considering various factors.",
    "Affordability and Flexibility": "The importance of affordability and policy flexibility is emphasized, maintaining a balance between coverage and budget constraints.",
    "Application Process": "The steps involved in the application process, requiring detailed information, are outlined by the agent.",
    "Term Duration and Medical Examination": "Discussions on term duration and the potential requirement for a medical examination during underwriting are provided.",
    "Riders and Additional Coverage": "The concept of riders and their role in customizing policies based on individual needs are explained, providing examples.",
    "Premium Payments and Beneficiary Updates": "Importance of timely premium payments and the flexibility to update beneficiaries are highlighted.",
    "Reviewing Policy and Financial Goals": "Suggestions for regular policy reviews and the potential for life insurance to support broader financial goals are provided.",
    "Tax Implications and Policy Adjustments": "General information on tax implications and the adaptability of policies to changing circumstances is offered.",
    "Finalizing and Moving Forward": "The client expresses readiness to proceed, and the agent assures ongoing support and clear understanding of the policy.",
    "Underwriting Process and Appeals": "The underwriting process and possibilities for appealing a decision are discussed, presenting alternatives.",
    "Policy Exclusions and Limitations": "The need to be aware of policy exclusions and limitations is highlighted for clear understanding.",
    "Cash Value and Financial Planning": "The potential for certain policies to accumulate cash value and support broader financial planning is explained.",
    "Transfers and Collateral Usage": "The possibility of transferring ownership and using cash value as collateral is introduced.",
    "Conclusion and Next Steps": "The client expresses gratitude and readiness to proceed, while the agent reassures ongoing commitment and prepares necessary paperwork.",
    "Coverage Activation and Duration": "Explanation of coverage activation timelines and general underwriting duration is provided.",
}
    df_schema, df_metadata = process_transcript(transcript, schema)
    return df_schema.to_html(), df_metadata.to_html()

def main():
    with gr.Blocks() as app:
        gr.Markdown("# Life Insurance Call Compliance Analysis")
        
        with gr.Row():
            transcript_input = gr.Textbox(label="Paste your transcript here", lines=10, placeholder="Paste transcript here...")
        
        with gr.Row():
            analyze_button = gr.Button("Analyze Call")

        with gr.Column():
            gr.Markdown("### Call Compliance Analysis")
            results_schema = gr.Markdown()  

            gr.Markdown("### Entity Analysis")
            results_metadata = gr.Markdown()  

            analyze_button.click(
                fn=analyze_transcript,
                inputs=[transcript_input],
                outputs=[results_schema, results_metadata]
            )

    app.launch()

if __name__ == "__main__":
    main()
