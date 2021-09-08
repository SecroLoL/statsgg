import React, { useEffect, useState } from 'react'
import axios from 'axios';

function Home() {
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/stats/matches').then((matches) => {
            console.log(matches);
            if (matches) {
                setMatches(matches)
            }
        }
        )
    });

    return (
        <div>
            <h1>Stats.gg</h1>
            {matches.data.map((match) => (
                <h1>match.championName</h1>
            ))}
        </div>
    )
}

export default Home
