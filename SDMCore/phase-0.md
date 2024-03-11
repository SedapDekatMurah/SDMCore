Phase 0 sprint, mar 17

PoC front end (React native)
- 1 Input field
- shows 1 result that matches
  - Option A: has profile (SDM rating)
  - Option B: no profile (Standard google maps)



PoC Back end
- Containerization
- API
  - GET restaurant (keyword), returns matching restaurant from
    - Option A: has profile. Return SDM profile
    - Option B: No profile, return generic Google maps 
- ML pipeline
  - Get new restaurant, add to database
    - Review keywords association
    - Prices for 2 menu items (STRETCH GOAL)
    - Travel distance


* Shortcomings: Database will be bootstrapped, i.e. no curated user input  


