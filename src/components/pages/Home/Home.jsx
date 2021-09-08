import React, { useEffect, useState } from 'react'
import axios from 'axios';

function Home() {
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/stats/matches').then((matches) => {
            if (matches.data) {
                console.log(matches.data);
                setMatches(matches.data);
            }
        }
        )
    }, []); // I'm assuming the , [] is alternate to when page is loaded.

    return (
        <div>
            <h1>Stats.gg</h1>
            {matches.map((match) => (
                <div key={match.totalDamageDealt}>
                    <h1>{match.championName}</h1>
                    <h2>Kda: <h3><span style={{color: 'green'}}>{match.kills}</span> / <span>{match.deaths}</span> / <span>{match.assists}</span> <span style={{color: {}}}>({match.deaths > 0 ? (match.kills + match.assists) / match.deaths : (match.kills + match.assists).toFixed(1)})</span></h3></h2>
                    <h2>Damage: <h3>{match.totalDamageDealt}</h3></h2>

                </div>

            ))}
        </div>
    )
}

export default Home
