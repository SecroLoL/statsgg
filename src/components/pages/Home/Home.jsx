import React, { useEffect, useState } from 'react'
import axios from 'axios';

function Home() {
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        axios.get('localhost:8000/stats').then((matches) => {
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
            {matches.forEach((match) => {
                <h1>match.championName</h1>
            })}
        </div>
    )
}

export default Home
