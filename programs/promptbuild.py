def build_prom(jsld):

    prom=f"""
You are a clinical trial analysis assistant.

Please analyze the following clinical trial information.

Study ID:
{jsld["study_id"]}

Study Title:
{jsld["study_title"]}

Study Population:
{jsld["population"]}

Treatment Being Evaluated:
{jsld["treatment"]}

Study Duration:
{jsld["duration"]}

Please provide:

1. A concise summary of the study.
2. The target population.
3. The treatment being evaluated.
4. The study duration.
5. Important observations about the study.

Do not make assumptions about information that is not provided.
"""

    return prom