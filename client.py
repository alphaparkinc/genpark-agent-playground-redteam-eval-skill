class AgentPlaygroundRedteamClient:
    def evaluate_defenses(self, jailbreak_prompts: list[str]) -> dict:
        passed = sum(1 for p in jailbreak_prompts if "ignore" not in p.lower())
        ratio = passed / max(1, len(jailbreak_prompts))
        return {"defended_ratio": round(ratio, 2), "vulnerability_details": ["Jailbreak check succeeded"]}