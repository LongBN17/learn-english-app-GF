import json

# IPA Mapping Dictionary
ipa_map = {
    # Idioms (approximate pronunciation for the whole phrase or key word stress)
    "piece of cake": "/piːs əv keɪk/",
    "break the ice": "/breɪk ðə aɪs/",
    "hit the nail on the head": "/hɪt ðə neɪl ɒn ðə hed/",
    "cost an arm and a leg": "/kɒst ən ɑːm ənd ə leɡ/",
    "let the cat out of the bag": "/let ðə kæt aʊt əv ðə bæɡ/",
    "kill two birds with one stone": "/kɪl tuː bɜːdz wɪð wʌn stəʊn/",
    "cutting corners": "/ˈkʌtɪŋ ˈkɔːnəz/",
    "miss the boat": "/mɪs ðə bəʊt/",
    "call it a day": "/kɔːl ɪt ə deɪ/",
    "hang in there": "/hæŋ ɪn ðeə/",
    "better late than never": "/ˈbetə leɪt ðæn ˈnevə/",
    "so far so good": "/səʊ fɑː səʊ ɡʊd/",
    "under the weather": "/ˈʌndə ðə ˈweðə/",
    "speak of the devil": "/spiːk əv ðə ˈdevl/",
    "time flies": "/taɪm flaɪz/",
    "on the ball": "/ɒn ðə bɔːl/",
    "burn the midnight oil": "/bɜːn ðə ˈmɪdnaɪt ɔɪl/",
    "once in a blue moon": "/wʌns ɪn ə bluː muːn/",
    "the best of both worlds": "/ðə best əv bəʊθ wɜːldz/",
    "see eye to eye": "/siː aɪ tu aɪ/",
    "rule of thumb": "/ruːl əv θʌm/",
    "out of the blue": "/aʊt əv ðə bluː/",
    "get something off your chest": "/ɡet ˈsʌmθɪŋ ɒf jɔː tʃest/",
    "go the extra mile": "/ɡəʊ ðə ˈekstrə maɪl/",
    "play it by ear": "/pleɪ ɪt baɪ ɪə/",
    "bite the bullet": "/baɪt ðə ˈbʊlɪt/",
    "climb the ladder": "/klaɪm ðə ˈlædə/",
    "keep an eye on": "/kiːp ən aɪ ɒn/",
    "give me a hand": "/ɡɪv mi ə hænd/",
    "in the same boat": "/ɪn ðə seɪm bəʊt/",

    # Advanced Tech
    "artificial intelligence": "/ˌɑːtɪfɪʃl ɪnˈtelɪɡəns/",
    "machine learning": "/məˈʃiːn ˈlɜːnɪŋ/",
    "neural network": "/ˈnjʊərəl ˈnetwɜːk/",
    "blockchain": "/ˈblɒk.tʃeɪn/",
    "cryptocurrency": "/ˈkrɪptəʊˌkʌrənsi/",
    "virtual reality": "/ˌvɜːtʃuəl riˈæləti/",
    "augmented reality": "/ɔːɡˌmentɪd riˈæləti/",
    "internet of things": "/ˈɪntənet əv θɪŋz/",
    "big data": "/ˌbɪɡ ˈdeɪtə/",
    "cloud computing": "/klaʊd kəmˈpjuːtɪŋ/",
    "cybersecurity": "/ˌsaɪbəsɪˈkjʊərəti/",
    "biometrics": "/ˌbaɪəʊˈmetrɪks/",
    "automation": "/ˌɔːtəˈmeɪʃn/",
    "robotics": "/rəʊˈbɒtɪks/",
    "quantum computing": "/ˈkwɒntəm kəmˈpjuːtɪŋ/",
    "ethics": "/ˈeθɪks/",
    "privacy": "/ˈprɪvəsi/",
    "surveillance": "/sɜːˈveɪləns/",
    "bandwidth": "/ˈbændwɪdθ/",
    "latency": "/ˈleɪtənsi/",
    "redundancy": "/rɪˈdʌndənsi/",
    "infrastructure": "/ˈɪnfrəstrʌktʃə/",
    "microservices": "/ˈmaɪkrəʊˌsɜːvɪsɪz/",
    "monolith": "/ˈmɒnəlɪθ/",
    "containerization": "/kənˌteɪnəraɪˈzeɪʃn/",
    "orchestration": "/ˌɔːkɪˈstreɪʃn/",
    "serverless": "/ˈsɜːvələs/",
    "devops": "/ˈdevɒps/",
    "continuous integration": "/kənˌtɪnjuəs ˌɪntɪˈɡreɪʃn/",
    "continuous deployment": "/kənˌtɪnjuəs dɪˈplɔɪmənt/",
    "legacy system": "/ˈleɡəsi ˈsɪstəm/",
    "refactoring": "/riːˈfæktərɪŋ/",
    "technical debt": "/ˈteknɪkl det/",
    "scalability": "/ˌskeɪləˈbɪləti/",
    "bottleneck": "/ˈbɒtlnek/",
    "throughput": "/ˈθruːpʊt/",
    "load balancing": "/ləʊd ˈbælənsɪŋ/",
    "failover": "/ˈfeɪləʊvə/",
    "uptime": "/ˈʌptaɪm/",
    "downtime": "/ˈdaʊntaɪm/",

    # General Advanced
    "ambitious": "/æmˈbɪʃəs/",
    "authentic": "/ɔːˈθentɪk/",
    "comprehensive": "/ˌkɒmprɪˈhensɪv/",
    "confidential": "/ˌkɒnfɪˈdenʃl/",
    "crucial": "/ˈkruːʃl/",
    "deliberate": "/dɪˈlɪbərət/",
    "elaborate": "/ɪˈlæbərət/",
    "fragile": "/ˈfrædʒaɪl/",
    "genuine": "/ˈdʒenjuɪn/",
    "inevitable": "/ɪnˈevɪtəbl/",
    "innovative": "/ˈɪnəveɪtɪv/",
    "mandatory": "/ˈmændətəri/",
    "meticulous": "/məˈtɪkjələs/",
    "obsolete": "/ˈɒbsəliːt/",
    "pragmatic": "/præɡˈmætɪk/",
    "prominent": "/ˈprɒmɪnənt/",
    "resilient": "/rɪˈzɪliənt/",
    "rigorous": "/ˈrɪɡərəs/",
    "simultaneous": "/ˌsɪmlˈteɪniəs/",
    "subtle": "/ˈsʌtl/",
    "sustainable": "/səˈsteɪnəbl/",
    "tedious": "/ˈtiːdiəs/",
    "temporary": "/ˈtemprəri/",
    "permanent": "/ˈpɜːmənənt/",
    "transparent": "/trænsˈpærənt/",
    "unanimous": "/juˈnænɪməs/",
    "unprecedented": "/ʌnˈpresɪdentɪd/",
    "versatile": "/ˈvɜːsətaɪl/",
    "vulnerable": "/ˈvʌlnərəbl/",
    "accumulate": "/əˈkjuːmjəleɪt/",
    "allocate": "/ˈæləkeɪt/",
    "anticipate": "/ænˈtɪsɪpeɪt/",
    "compensate": "/ˈkɒmpenseɪt/",
    "consolidate": "/kənˈsɒlɪdeɪt/",
    "contradict": "/ˌkɒntrəˈdɪkt/",
    "deviate": "/ˈdiːvieɪt/",
    "diminish": "/dɪˈmɪnɪʃ/",
    "eliminate": "/ɪˈlɪmɪneɪt/",
    "emphasize": "/ˈemfəsaɪz/",
    "enhance": "/ɪnˈhɑːns/",
    "establishing": "/ɪˈstæblɪʃɪŋ/",
    "evaluate": "/ɪˈvæljueɪt/",
    "exaggerate": "/ɪɡˈzædʒəreɪt/",
    "facilitate": "/fəˈsɪlɪteɪt/",
    "fluctuate": "/ˈflʌktʃueɪt/",
    "generate": "/ˈdʒenəreɪt/",
    "ignore": "/ɪɡˈnɔː/",
    "imply": "/ɪmˈplaɪ/",
    "initiate": "/ɪˈnɪʃieɪt/"
}

def update_ipa():
    try:
        with open('data/content.json', 'r', encoding='utf-8') as f:
            content = json.load(f)
    except FileNotFoundError:
        print("data/content.json not found!")
        return

    updated_count = 0
    missing_ipa_count = 0
    
    for item in content:
        if item.get('type') == 'word':
            term = item.get('term', '').lower()
            current_ipa = item.get('ipa', '')
            
            # Check if IPA is missing or placeholder
            if not current_ipa or current_ipa == "N/A":
                if term in ipa_map:
                    item['ipa'] = ipa_map[term]
                    updated_count += 1
                else:
                    missing_ipa_count += 1
                    # print(f"Missing IPA definition for: {term}")

    with open('data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    print(f"Updated {updated_count} words with IPA.")
    print(f"Still missing {missing_ipa_count} words (might need manual check).")

if __name__ == "__main__":
    update_ipa()
