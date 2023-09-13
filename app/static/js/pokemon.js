document.addEventListener("DOMContentLoaded", function () {
    let isShiny = false;
    const pokemonForm = document.getElementById("pokemonForm");
    const pokemonImageDiv = document.getElementById("pokemonImageDiv");
    const pokemonStats = document.getElementById("pokemonStats");
    const toggleShinyBtn = document.getElementById("toggleShiny");

    const fetchPokemonInfo = async (pokemonName) => {
        try {
            const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
            if (response.ok) {
                const pokemon = await response.json();

                const imageUrl = isShiny ? pokemon.sprites.front_shiny : pokemon.sprites.front_default;
                pokemonImageDiv.innerHTML = `<img src="${imageUrl}" alt="${pokemonName}" />`;
                const statsHtml = `
                <ul>
                    <li>HP: ${pokemon.stats[0].base_stat}</li>
                    <li>Attack: ${pokemon.stats[1].base_stat}</li>
                    <li>Defense: ${pokemon.stats[2].base_stat}</li>
                    <li>Special Attack: ${pokemon.stats[3].base_stat}</li>
                    <li>Special Defense: ${pokemon.stats[4].base_stat}</li>
                    <li>Speed: ${pokemon.stats[5].base_stat}</li>
                </ul>
                `;
                pokemonStats.innerHTML = statsHtml;
            } else {
                console.error(`Failed to fetch data: ${response.status}`);
            }
        } catch (error) {
            console.error(`An error occurred: ${error}`);
        }
    };

    pokemonForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        const pokemonName = document.getElementById("pokemonInput").value;
        fetchPokemonInfo(pokemonName);
    });

    toggleShinyBtn.addEventListener("click", function () {
        isShiny = !isShiny;
        const currentPokemon = document.getElementById("pokemonInput").value;
        if (currentPokemon) {
            fetchPokemonInfo(currentPokemon);
        }
    });
});
