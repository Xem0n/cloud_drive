import { ChangeEvent, Dispatch, SetStateAction } from 'react';
import './Text.css';

const FILLED_CLASS = 'filled';

type TextProps = {
    name: string;
    type: string;
    value: string;
    onChange: Dispatch<SetStateAction<string>>;
    placeholder?: string;
    required?: boolean;
};

const Text = (props: TextProps) => {
    const onChange = (event: ChangeEvent<HTMLInputElement>) => {
        props.onChange(event.target.value);
    };

    const isFilled = (): string => (
        props.value !== '' ? FILLED_CLASS : ''
    );

    return (
        <div className='input-container'>
            <input 
                className='input-text'
                name={props.name}
                id={props.name}
                type={props.type}
                value={props.value}
                onChange={onChange}
                required={props.required || false} />

            <label 
                className={'input-placeholder ' + isFilled()} 
                htmlFor={props.name}>
                {props.placeholder || ''}
            </label>
        </div>
    );
};

export default Text;