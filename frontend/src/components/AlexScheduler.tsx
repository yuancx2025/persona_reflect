import { useState } from "react";
import { api, CalendarSlot } from "@/services/api";

export function AlexScheduler() {
    const [slots, setSlots] = useState<CalendarSlot[]>([]);
    const [alexText, setAlexText] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleSchedule() {
        setLoading(true);
        const { alex, slots } = await api.alexSchedule("I need 90min deep work this week");
        setAlexText(alex);
        setSlots(slots);
        setLoading(false);
    }

    async function handleBook(slot: CalendarSlot) {
        const evt = await api.alexBookEvent("Deep Work", slot.start, 90, "From PersonaReflect");
        window.open(evt.htmlLink, "_blank");
    }

    return (
        <div className="p-4 rounded-xl shadow-md bg-white">
            <h2 className="font-semibold text-lg mb-2">📊 Rational Analyst — Alex</h2>

            <button
                onClick={handleSchedule}
                className="px-4 py-2 bg-blue-500 text-white rounded"
                disabled={loading}
            >
                {loading ? "Analyzing..." : "Ask Alex for Schedule"}
            </button>

            {alexText && <p className="mt-3 text-gray-700 whitespace-pre-line">{alexText}</p>}

            <div className="mt-3">
                {slots.map((slot) => (
                    <button
                        key={slot.start}
                        onClick={() => handleBook(slot)}
                        className="block w-full text-left border rounded p-2 mb-2 hover:bg-gray-100"
                    >
                        {slot.label} — {new Date(slot.start).toLocaleString()}
                    </button>
                ))}
            </div>
        </div>
    );
}
